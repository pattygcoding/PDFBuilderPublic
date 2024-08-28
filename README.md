# PDFBuilderPublic
I made this in May 2024 to generate ATS-friendly tailored resumes on demand at lightning speed. This is the public repo for the work I have done.

## Dependencies
To successfully run this script, you will need to install Python, and also these pip libraries:

pdfkit:
```
pip install pdfkit
```

jinja2:
```
pip install jinja2
```

## Instructions
To create an ATS-friendly and Workday Parse Format Resume in a folder called "CompanyName":
```
python convert.py CompanyName
```

To create an ATS-friendly and Workday Parse Format Resume in the main directory:
```
python convert.py
```

To change the contents of the resume, edit the JSON file according to your needs.
