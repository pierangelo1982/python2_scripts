# coding=utf-8
from __future__ import division

totale = 0
contatore = 0

alunni = input("inserisci numero alunni: ")

while contatore <= alunni:
    voto = input("inserisci il voto: ")
    totale += voto
    contatore += 1

#media = totale / alunni
media = float(totale / contatore)
print contatore, "alunni con media di", media
