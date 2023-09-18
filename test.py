import PyPDF2
import pdfquery
import pandas as pd
import PyPDF2
from PyPDF2 import PdfReader
from pdf2image import convert_from_path, convert_from_bytes
import pytesseract
from PIL import Image
from lxml import etree
pdf = pdfquery.PDFQuery('C:\\Users\\samir\\Desktop\\stage\\test.pdf')
pdf.load()
pdf.tree.write('pdfXML.txt', pretty_print = True)
# Example selector to extract text from a specific element with id "my_element_id"
selector = "#Monsieur"
result = pdf.pq(selector).text()

# If you want to extract data from multiple elements matching the selector:
elements = pdf.pq(selector)
for element in elements:
    print(element.text)