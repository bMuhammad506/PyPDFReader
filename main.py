from PyPDF2 import PdfReader
from pdfminer.high_level import extract_text
import pdfplumber as pdfplm

print('PyPDF2')
reader = PdfReader("COVID19-symptoms.pdf")
number_of_pages = len(reader.pages)
for i in range(0,number_of_pages):
    page = reader.pages[i]
    text = page.extract_text()
    print(text)

print('\n pdf miner')
text = extract_text('COVID19-symptoms.pdf')
print(text)

print('\n PDF plumber')
with pdfplm.open('COVID19-symptoms.pdf') as pdf:
    nopages = len(pdf.pages)
    for i in range(0,nopages):
        print(pdf.pages[i].extract_text())

