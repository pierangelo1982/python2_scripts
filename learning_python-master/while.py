# coding=utf-8
from __future__ import division

totale = 0
contatore = 0

while contatore <= 5:
    voto = input("inserisci voto: ")
    totale = totale + voto
    contatore = contatore + 1

media = float(totale / 5)
print "la media è di: ", media
print "il contatore è:", contatore
