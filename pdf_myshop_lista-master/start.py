__author__ = 'pierangelo orizio'

import json
import urllib
from connection import *
from fpdf import FPDF


data = connessione("https://myshopfurniture.com/api/moduli/")
print(data)


pdf = FPDF()
pdf = FPDF('L', 'mm', 'A4')
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)

pdf.cell(150, 10, "Descrizione", 1)
pdf.cell(50, 10, "Misure", 1, 1)

for d in data:
    pdf.cell(150, 10, d["fields"]["name"], 1)
    pdf.cell(50, 10, d["fields"]["size"], 1, 1)

pdf.output('tuto2.pdf', 'F')






for d in data:
	print(d["fields"]["name"])

