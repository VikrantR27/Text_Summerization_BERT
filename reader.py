import PyPDF2 
import textract
from docx import Document 

def PDFRead(filepath): 
    pdfFileObj = open(filepath, 'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    x=pdfReader.numPages
    for i in range(x): 
        pageObj = pdfReader.getPage(i) 
        print(pageObj.extractText()) 
    pdfFileObj.close() 

def DOCRead(filepath):
    document = Document(filepath)
    for para in document.paragraphs:
        print(para.text)


# PDFRead("ENTER_FILE_PATH")
# DOCRead("ENTER_FILE_PATH")