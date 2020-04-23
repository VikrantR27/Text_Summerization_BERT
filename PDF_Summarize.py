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

def DOCRead(filepath):
    document = Document(filepath)
    file=""
    for para in document.paragraphs:
        file=file+para.text
    
    return(file)


text1 = "YOUR_FILE_PATH"

if text1[-3]+text1[-2]+text1[-1]=="pdf" :
    text=PDFRead(text1)

if text1[-4]+text1[-3]+text1[-2]+text1[-1]=="docx" :
    text=DOCRead(text1)
    

print(text)
model = Summarizer('distilbert-base-uncased')
summary = model(text)

print(summary)