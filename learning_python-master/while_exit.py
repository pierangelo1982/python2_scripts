# coding=utf-8
from __future__ import division

totale = 0
contatore = 0
voto = 0

while voto != -2:
    voto = input("Inserisci il voto, -2 per uscire: ")
    totale += voto
    contatore += 1

media = float(totale / contatore)
print contatore, "voti inseriti, la media è di:", media