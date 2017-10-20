from bs4 import BeautifulSoup
import urllib3
from random import randint
import sys

#http = urllib3.PoolManager()
#response = http.request('GET', "http://www.edupedia.pl/map/dictionary/id/8_slownik_wyrazow_obcych.html")
#soup = BeautifulSoup(response.data, "lxml")

slowa = []
linki = []
with open('slowa_obce.txt', 'r') as f:
    for line in f:
        slowa.append(line.strip())
print(len(slowa))

with open('slowa_obce_linki.txt', 'r') as f:
    for line in f:
        linki.append(line.strip())
print(len(linki))



#for link in soup.find_all("a",{'class': 'lkyDescLink'} ):
#    tytuly.append(link.text.strip())
    
#for link in soup.find_all("a",{'class': 'lkyDescLink'} ):
#    linki.append(link.get('href'))

#tytuly1 = tytuly[11:]
#linki1 = linki[11:]
#print(tytuly[11:])
#print(linki[11:])
#print(len(tytuly1))

#for i in range(5):
#    liczexp.append(randint(0,10571))

#print(liczexp)

#zapisuje poniższe do pliku:
#sys.stdout = open('slowa_obce.txt','wt')
#for i in range(len(tytuly1)):
#    print(tytuly1[i])

#sys.stdout = open('slowa_obce_linki.txt','wt')
#for i in range(len(tytuly1)):
#    print(linki1[i])
