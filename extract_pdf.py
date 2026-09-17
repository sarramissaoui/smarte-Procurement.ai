import os
import PyPDF2

def extract_text_from_folder(pdf_folder):
    tenders_text = {}

    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith('.pdf'):
            path = os.path.join(pdf_folder, pdf_file)

            with open(path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""

                for page in reader.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + "\n"

            tenders_text[pdf_file] = text

    return tenders_text