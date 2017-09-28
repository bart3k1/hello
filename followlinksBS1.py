from bs4 import BeautifulSoup
import urllib3
import sys

start = input("Linka startowa: ")
ile_art = int(input("Ile artykułów?: "))
http = urllib3.PoolManager()
response = http.request('GET', 'http://dziendobry.tvn.pl' + start)
soup = BeautifulSoup(response.data, "lxml")

tagi = {}
tytuly = []
leady = []
linki = []
linki.append(start)
counter = 0

while counter < ile_art:
    response = http.request('GET', 'http://dziendobry.tvn.pl' + linki[-1])
    soup = BeautifulSoup(response.data, "lxml")

    for link in soup.find_all("h4",{'class': 'detail__title'} ):
        tytuly.append(link.text.strip())

    for link in soup.find_all("div",{'class': 'detail__short'} ):
        leady.append(link.text.strip())

    for link in soup.find_all("a",{'class': 'source__tag'} ):
        tagi[link.text.strip()]= link.get('href')

    for link in soup.find_all("a",{'title': 'Następny artykuł'} ):
        if not link.get('href') in linki:
            linki.append(link.get('href'))
    counter += 1

print(tagi)
print(tytuly)
print(leady)
print(linki)

#zapisuje poniższe do pliku:
sys.stdout = open('ddtvn.txt','wt')
for i in range(len(tytuly)):
    print(tytuly[i], '\n'+leady[i], '\n'+'http://dziendobry.tvn.pl'+linki[i])


