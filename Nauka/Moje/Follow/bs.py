from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'http://dziendobry.tvn.pl/wideo,2064,n/jerzy-dudek-poszedl-do-szkoly,242247.html')
soup = BeautifulSoup(response.data, "lxml")

print("HEAD")
#print(soup.head)
#print(soup.title)
#print(soup.body)
#print(soup.body.div)

print("Paragraf")
#print(soup.p)
#print(soup.h2)

print('\n FIND ALL')
#print(soup.find_all('p'))
#print(soup.find_all('header'))

print('\n FIND 1')
#print(soup.find(id="filterSelected"))
#print("Całość")
#print(soup)

print('\n FIND  ALL LINKS')

#for link in soup.find_all("a"):
#    print(link.get('href'))

#print('\n CAŁY TEXT')
#print(soup.get_text())

a = soup.head
#print(a)
#print(a.contents)
#print(len(a.contents))
#print(a.contents[1])
#print(a.contents[1].type)
#for i in a.contents:
#    print(i)

b = soup.a
#print(b)
for i in b:
    print(i)

#Wszystkie linki
c = soup.find_all('a')
print(c)

#Najnowsze in linki
for i in c:
    if "Najnowsze" in i:
        print(i)

#Pomoc in linki
for i in c:
    if "Pomoc" in i:
        print(i)

#Hrefy linkow
for i in c:
    print(i.get('href'))

#Klasy LINKOW
for i in c:
    print(i.get('class'))

#Title LINKOW
for i in c:
    print(i.get('title'))

for i in c:
    if i.get('title') == "Czat":
        print(i)
for i in c:
    if i.get('title') == "Zaloguj się przez Facebooka":
        print(i)
