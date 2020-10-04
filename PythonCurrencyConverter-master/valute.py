import sys
import feedparser
### Dollaro
feeddollaro = feedparser.parse("http://www.ecb.int/rss/fxref-usd.html")
### Sterlina
feedsterlina = feedparser.parse("http://www.ecb.europa.eu/rss/fxref-gbp.html")
### Yen Giapponese
feedyen = feedparser.parse("http://www.ecb.europa.eu/rss/fxref-jpy.html")

'''
###vedi giusto
print feeddollaro.entries[0].title[0:6]
print feedsterlina.entries[0].title[0:6]
print feedyen.entries[0].title[0:6]
### Cambio Monete
monete = {'sterlina': feedsterlina.entries[0].title[0:6],
      	'dollaro': feeddollaro.entries[0].title[0:6],
      	'yen': feedyen.entries[0].title[0:6]}
cifra = input('inserisci valore in Euro da convertire: ')
domanda = raw_input('Inserisci dollaro, sterlina, yen: ')
valore = monete.get(domanda)
print cifra*(float(valore))

'''

cifra = input('inserisci valore in Euro da convertire: ')

class Valute:
	sterlina = float(feedsterlina.entries[0].title[0:6])*cifra
	dollaro = float(feeddollaro.entries[0].title[0:6])*cifra
	yen = float(feedyen.entries[0].title[0:6])*cifra

print ("Sterline ="), Valute.sterlina
print ("Dollaro = "), Valute.dollaro
print ("Yen ="), Valute.yen
