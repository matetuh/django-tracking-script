import requests
from bs4 import BeautifulSoup
import re
pattern = re.compile(r'\s+')


URL = 'https://www.olx.pl/oferty/q-sony-a7ii/?search%5Border%5D=filter_float_price%3Aasc'

headers = {"User-Agnet": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

def check_price():

    # in lista1 list we get 
    lista1 = []
    for url in soup.findAll("a", {"class":"marginright5 link linkWithHash detailsLink"}):
        lista1.append(url.get("href"))

    lista = []
    for link in soup.findAll('strong'):
        lista.append(link.text)

    # removing from the table this words
    lista.remove("")
    lista.remove("")
    lista.remove("Mój OLX")
    lista.remove("To ogłoszenie nie jest już dostępne")
    lista.remove("Google Play")
    lista.remove("AppStore")
    lista.remove("Wyszukiwanie zostało dodane do obserwowanych")
    lista.remove("Ogłoszenie dodane do obserwowanych")
    lista.remove("")
    lista.remove("AppGallery")

    # dividing the "lista" list to 2 lists -> lista4 (the headers) and lista3 (the prices)
    lista3 = []
    lista4 = []
    for i in range(len(lista)):
        if (i%2 != 0):
            lista3.append(lista[i])
        else:
            lista4.append(lista[i])
    lista3.remove(lista3[0])
    lista4.remove(lista4[0])

    for i in range(len(lista3)):
        lista3[i] = re.sub(pattern, '', lista3[i])

    for i in range(len(lista1)):
        # the price condition of the camera
        if (3000>int(lista3[i][:-2])>1000):
            print(lista4[i])
            print(lista3[i])
            print(lista1[i])
            print("-----------------------")
            


check_price()