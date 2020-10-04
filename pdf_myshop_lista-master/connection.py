import urllib
import json


def connessione(url):
	try:
		url = url
		response = urllib.urlopen(url)
		data = json.loads(response.read())
		return data
	except:
		return 0