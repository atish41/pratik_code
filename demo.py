import pdfkit

# HTML content to convert
html_content = "<h1>Hello World</h1>"

# Path to wkhtmltopdf executable
wkhtmltopdf_path = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

# Configuration
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

# Output PDF path
output_pdf_path = "test_output.pdf"

# Create PDF from HTML content
pdfkit.from_string(html_content, output_pdf_path, configuration=config)
