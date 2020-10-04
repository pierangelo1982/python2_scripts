# coding=utf-8
__author__ = 'pierangelo'

import os
import re
from os import path
import pykml
from pykml import parser
import lxml
from fastkml import kml


# leggo il file kml
def importakml(kml_file):
    doc = file(kml_file).read()
    return doc


# definisco il tag colore
def getcolore(doc):
    tag = re.findall(r"(?<=<color>)(.*?)(?=</color>)", doc)
    return tag


# definisco il tag del marker
def getmarker(doc):
    tag = re.findall(r"(?<=<href>)(.*?)(?=</href>)", doc)
    return tag



## importo il KML originale
percorso = path.join("sellaronda.kml")
imp = importakml(percorso)
## creo un kml con modifiche
out = open("out.kml", 'w')  # out file

# ## creo l'array con i colori presenti nel KML
tag_colore = getcolore(imp)

## lista dei colori ottenuti, rimpiazzo il colore e scrivo dentro imp,
## imp, ovvero stringa del KML originale che poi salvo nel nuovo kml.
for x in tag_colore:
    editdoc = imp.replace(x, "00000000")

# write fuori dal loop perchè altrimenti salvava tutto kml per numero dei loop
out.write(editdoc)
out.close()

# apro kml appena generato
path_out = path.join("out.kml")
imp = importakml(path_out)

## nuovo file kml
outmarker = open("outmarker.kml", 'w')  # out file

tag_marker = getmarker(imp)
print(tag_marker)

for t in tag_marker:
    editmarker = imp.replace(t, "http://cyclingpassion.net/static/img/marker/red.png")
    print t

#write fuori dal loop perchè altrimenti salvava tutto kml per numero dei loop
outmarker.write(editmarker)
outmarker.close()

