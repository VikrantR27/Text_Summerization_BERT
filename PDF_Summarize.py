import torch
from summarizer import Summarizer
import PyPDF2 
import textract
from docx import Document 

def PDFRead(filepath): 
    pdfFileObj = open(filepath, 'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    x=pdfReader.numPages
    file=""
    for i in range(x): 
        pageObj = pdfReader.getPage(i) 
        file=file+pageObj.extractText()
    pdfFileObj.close() 
    return(file)

text1 = PDFRead("FILE_PATH")
print(text)
model = Summarizer('distilbert-base-uncased')
summary = model(text)

print(summary)