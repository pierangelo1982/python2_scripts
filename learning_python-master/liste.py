import os
import smtplib



elenco = [9, 1, 1982]
print elenco


#lista che contiene altra lista
elenco = [9, 1, 1982]
varie = [1, "pierangelo", elenco]
print varie


#estrarre lista con libreria
varie.append(smtplib)
print varie;

#estrarre elementi dalla lista
data_nascita = [9, 1, 1982]
giorno = [0]
mese = [1]
anno = [2]
print giorno
print mese
print anno

# comandi - su lista
print data_nascita[-1]  #parte dal fondo della lista
print data_nascita[-2] #parte da in fondo -2 quindi vedi il mese
print data_nascita[+1] #parte dal primo con + 1 quindi anche cosi mostra mese

#ricostruire le variabili giorno, mese, anno con il metodo sopra
giorno = data_nascita[-3]
mese = data_nascita[-2]
anno = data_nascita[-1]
print giorno
print mese
print anno

#comando len per vedere lunghezza di una lista
len(data_nascita)
print len(data_nascita)


#partire da
print data_nascita[:1]

#ottenere giorno, mese, anno con metodo sopra
giorno = data_nascita[0:1]
mese = data_nascita[1:2]
anno = data_nascita[2:3]
print "giorno: ", giorno
print "mese: ", mese
print "anno: ", anno