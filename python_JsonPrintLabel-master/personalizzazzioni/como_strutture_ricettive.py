# -*- coding: utf8 -*-


__author__ = 'pierangelo orizio'

import json
import urllib
from fpdf import FPDF


url = "https://www.dati.lombardia.it/resource/graj-ggfx.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data


## config pdf format  ####
pdf = FPDF('L', 'mm', (110, 220))

for dato in data:
    if dato['classificazione'] == "Alberghi 2 stelle":
        denominazione = dato['denominazione_struttura']
        if 'indirizzo' in dato:
            indirizzo = dato['indirizzo']
        if 'cap' in dato:
            comune = dato['cap'] + " " + dato['nome_comune'] + "(" + dato['provincia'] + ")"

        print(denominazione)
        if 'indirizzo' in dato:
            print(indirizzo)
        if 'cap' in dato:
            print(comune)
        print("")

        pdf.add_page() ## generate pages from loop
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(200, 20, "Spett.le:")
        pdf.ln(7)
        pdf.cell(200, 20, denominazione)
        if 'indirizzo' in dato:
            if dato['indirizzo'].decode('utf8'):
                pdf.ln(7)
                pdf.cell(200, 20, indirizzo, 'L')
        if 'cap' in dato:
            pdf.ln(7)
            pdf.cell(200, 20, comune, 'L')

# save pdf
pdf.output('Alberghi_2_stelle.pdf', 'F')