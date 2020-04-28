import torch
from summarizer import Summarizer
import PyPDF2 
import textract
from docx import Document 
import pytesseract
from PIL import Image

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

def IMGRead(filepath):
    img=Image.open(filepath)
    text=pytesseract.image_to_string(img)
    return (text)

text1 = "1.png"

if text1[-3]+text1[-2]+text1[-1]=="pdf" :
    text=PDFRead(text1)

if text1[-4]+text1[-3]+text1[-2]+text1[-1]=="docx" :
    text=DOCRead(text1)

if text1[-3]+text1[-2]+text1[-1]=="png" :
    text=IMGRead(text1)

if text1[-4]+text1[-3]+text1[-2]+text1[-1]=="jpeg" :
    text=IMGRead(text1)

    

print(text)
model = Summarizer('distilbert-base-uncased')
summary = model(text)

print(summary)