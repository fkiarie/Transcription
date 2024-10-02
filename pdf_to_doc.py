from pdf2docx import Converter
import os

# List of PDF files you want to convert (you can specify a folder and automate it to get all PDFs)
pdf_files = [
    r"file1.pdf",
    r"file2.pdf",
    r"file3.pdf"
]

# Folder where DOCX files will be saved
output_folder = r"C:\Users\DELL\Desktop\INTERNSHIP\Converted_Documents"

# Ensure the output folder exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Batch convert each PDF to DOCX
for pdf_file in pdf_files:
    # Extract the base name of the PDF (without extension) to use it as the DOCX file name
    base_name = os.path.basename(pdf_file).replace(".pdf", "")
    
    # Construct the full path for the output DOCX file
    docx_file = os.path.join(output_folder, f"{base_name}.docx")
    
    # Convert the PDF to DOCX
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()

    print(f"Converted: {pdf_file} to {docx_file}")

print("Batch conversion complete!")
