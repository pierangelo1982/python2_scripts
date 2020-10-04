# coding=utf-8


# formula:
# da destra a sinistra, gli 1 vengono elevati a potenza (2 potenza numeri
# posizione da destra a sinistra)
#Esempio 11000000 - 2 elevato alla 6 perchè ci sono 6 posizioni per arrivare all'uno


decimale = "11000000"
contatore = len(decimale)
implemento = 0
risultato = 0
#print contatore

# misuro la lunghezza del decimale, poi eseguo un loop che lo decrementa per la
# lunghezza e infime passo il numero che si decrementa per ottenere la singola
# cifra
while contatore > 0:
    contatore -= 1
    if  decimale[contatore] == '1':
        risultato += 2 ** implemento
    implemento += 1 #incremento x sapere numeri precedenti da elevare a potenza
    print risultato

print("il risultato è: %i" %  risultato)



