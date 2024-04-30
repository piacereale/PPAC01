import requests
from Flask import request, flask
risposta= requests.get('https://meteo.lastampa.it')  # ma il sito della stampa non è l'ideale per questo lavoro
print(risposta)
print(risposta.text)
