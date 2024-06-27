from weasyprint import HTML

def create_pdf_with_weasyprint(html_content, output_path):
    HTML(string=html_content).write_pdf(output_path)

html_content = "<h1>Hello, this is a PDF created using WeasyPrint!</h1>"
output_pdf_path = "output_weasyprint.pdf"

create_pdf_with_weasyprint(html_content, output_pdf_path)
