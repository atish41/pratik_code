import streamlit as st
import google.generativeai as genai
import PyPDF2
from fpdf import FPDF
import unicodedata
import pdfkit
import markdown2
#from encode_fun import encode_pdf_to_base64
from test import extract_text_from_pdf

# Function to extract text from the first page of a PDF
def extract_text_from_first_page(pdf_file):
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        first_page = reader.pages[0]
        text = first_page.extract_text()
        if text:
            return text
        else:
            raise ValueError("No text found on the first page.")
    except Exception as e:
        st.error(f"Error extracting text: {e}")
        return None

# Function to create a PDF from text with UTF-8 encoding
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Filled Form Details', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def create_pdf(text, output_path):
    pdf = PDF()
    pdf.add_page()
    pdf.chapter_title('Form Details')
    pdf.chapter_body(text)
    pdf.output(output_path)

# Function to convert text to be latin-1 compatible
def convert_to_latin1_compatible(text):
    # Replace the en-dash with a hyphen
    text = text.replace('\u2013', '-')
    
    # Normalize and encode to latin-1, ignoring unsupported characters
    text = unicodedata.normalize('NFKD', text).encode('latin-1', 'ignore').decode('latin-1')
    
    return text

def create_pdf_from_html(html_content, output_path, wkhtmltopdf_path):
    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
    pdfkit.from_string(html_content, output_path, configuration=config)

# Configure the Generative AI model with API key
api_key = "AIzaSyBwzbkNHte8dSjSl9Ds7_aoxcTU20PH61g"  # Replace with your actual API key
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit app
st.title('Visa Form Filling')

st.header('Upload Questionnaire and Form')
uploaded_questionnaire = st.file_uploader("Upload Questionnaire PDF", type="pdf")
uploaded_form = st.file_uploader("Upload Form PDF", type="pdf")

if uploaded_questionnaire is not None and uploaded_form is not None:
    if st.button('Generate Filled Form'):
        encodedpdf1 = extract_text_from_pdf(uploaded_questionnaire.read())
        encodedpdf2 = extract_text_from_pdf(uploaded_form.read())

        prompt1 = "Please go through all the information provided below for a person"
        prompt2 = "Output the field from with all the respective fields and try to fill all the details that you find in the information document"
        
        # Generate content using the Generative Model
        response = model.generate_content([prompt1, encodedpdf1, prompt2, encodedpdf2])

        # Resolve the response
        response.resolve()
        filled_details = response.text

        # Convert to latin-1 compatible text
        filled_details_latin1 = convert_to_latin1_compatible(filled_details)

        st.subheader('Filled Form Details')
        st.text(filled_details_latin1)

        html_content=markdown2.markdown(filled_details_latin1)

        # Convert the filled details to PDF
        output_pdf_path = "filled_form_details.pdf"
        #create_pdf(filled_details_latin1, output_pdf_path)
        #create_pdf(html_content, output_pdf_path)

        wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Update this path if necessary
        output_pdf_path = "visa_roadmap.pdf"

            # Create PDF from HTML content
        create_pdf_from_html(html_content, output_pdf_path, wkhtmltopdf_path)

        with open(output_pdf_path, "rb") as pdf_file:
            st.download_button(
                label="Download Filled Form Details as PDF",
                data=pdf_file,
                file_name="filled_form_details.pdf",
                mime="application/pdf"
            )
