__author__ = 'pierangelo orizio'

import json
import urllib
from fpdf import FPDF


url = "https://www.dati.lombardia.it/resource/xy9p-k9bj.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data


## config pdf format  ####
#pdf = FPDF()
#pdf = FPDF('L', 'mm', 'Letter')
pdf = FPDF('L', 'mm', (110, 220))

for count in data:
    print(count['nome_agriturismo'])
    print(count['cap_com_pro'])
    #in some array of json key 'indirizzo_completo' is missed
    if 'indirizzo_completo' in count:
        print(count['indirizzo_completo'])
    else:
        print("indirizzo nullo")
    print("")

    pdf.add_page() ## generate pages from loop
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 20, "Spett.le:")
    pdf.ln(7)
    pdf.cell(200, 20, count['nome_agriturismo'])
    if 'indirizzo_completo' in count:
        pdf.ln(7)
        pdf.cell(200, 20, count['indirizzo_completo'], 'L')
    pdf.ln(7)
    pdf.cell(200, 20, count['cap_com_pro'], 'L')

# save pdf
pdf.output('buste.pdf', 'F')
