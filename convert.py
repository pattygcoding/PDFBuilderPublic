import json
import os  # Import os for directory operations
import pdfkit
from jinja2 import Template
import sys  # Import sys to handle command-line arguments

def load_template(template_path):
    # Load the HTML template from a file
    with open(template_path, 'r') as file:
        return Template(file.read())

def convert(template, json_data):
    # Render the HTML with the JSON data
    return template.render(json_data=json_data)

def save_pdf(html_content, output_path):
    # Save the HTML content as a PDF file
    pdfkit.from_string(html_content, output_path)

def main(company_name=None):
    # File paths
    input_json_file = 'data.json'
    resume_template_file = 'resume.html'
    workday_template_file = 'workday.html'
    
    # Determine output directory and file paths
    if company_name:
        output_dir = os.path.join(os.getcwd(), company_name)
        os.makedirs(output_dir, exist_ok=True)
        output_pdf_file = os.path.join(output_dir, 'Patrick Goodwin Resume.pdf')
        output_pdf_file_wd = os.path.join(output_dir, 'Patrick Goodwin Resume WD.pdf')
    else:
        output_pdf_file = 'Patrick Goodwin Resume.pdf'
        output_pdf_file_wd = 'Patrick Goodwin Resume WD.pdf'
    
    # Load JSON data from a file using standard json
    with open(input_json_file, 'r') as f:
        json_data = json.load(f)
    
    # Load the HTML templates
    resume_template = load_template(resume_template_file)
    workday_template = load_template(workday_template_file)
    
    # Convert JSON data to HTML
    resume_html_content = convert(resume_template, json_data)
    workday_html_content = convert(workday_template, json_data)
    
    # Save HTML content as PDFs
    save_pdf(resume_html_content, output_pdf_file)
    save_pdf(workday_html_content, output_pdf_file_wd)
    
    print(f'PDF generated: {output_pdf_file}')
    print(f'PDF generated: {output_pdf_file_wd}')

if __name__ == '__main__':
    # Check for optional command-line argument for the company name
    if len(sys.argv) > 1:
        company_name = sys.argv[1]
    else:
        company_name = None
    main(company_name)
