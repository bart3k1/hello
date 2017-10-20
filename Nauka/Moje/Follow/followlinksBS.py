from bs4 import BeautifulSoup
import urllib3
start = input("Linka startowa: ")
http = urllib3.PoolManager()
response = http.request('GET', 'http://dziendobry.tvn.pl' + start)
soup = BeautifulSoup(response.data, "lxml")

tagi = {}
tytuly = []
leady = []
linki = []

#print("TYTUŁ")
for link in soup.find_all("h4",{'class': 'detail__title'} ):
    #print(link.text.strip())
    tytuly.append(link.text.strip())
#print()

#print("LEAD")
for link in soup.find_all("div",{'class': 'detail__short'} ):
    #print(link.text.strip())
    leady.append(link.text.strip())
#print()

#print("TAGI Z TEKSTEM")
for link in soup.find_all("a",{'class': 'source__tag'} ):
    #print(link.text.strip())
    #print(link.get('href'))
    tagi[link.text.strip()]= link.get('href')
#print()

#print("NXT BEZ TEKSTU... JESZCZE")

nst_art_link = []
for link in soup.find_all("a",{'title': 'Następny artykuł'} ):
    #print(link.get('href'))
    if not link.get('href') in nst_art_link:
        nst_art_link.append(link.get('href'))
#print(nst_art_link)

#print()
#print(">>> Przechodzimy dalej! <<<")
#print()
counter = 0
while counter < 10:
    response = http.request('GET', 'http://dziendobry.tvn.pl' + nst_art_link[0])
    soup = BeautifulSoup(response.data, "lxml")

    #print("TYTUŁ")
    for link in soup.find_all("h4",{'class': 'detail__title'} ):
        #print(link.text.strip())
        tytuly.append(link.text.strip())
    #print()

    #print("LEAD")
    for link in soup.find_all("div",{'class': 'detail__short'} ):
        #print(link.text.strip())
        leady.append(link.text.strip())
    #print()

    #print("TAGI Z TEKSTEM")
    for link in soup.find_all("a",{'class': 'source__tag'} ):
        #print(link.text.strip())
        #print(link.get('href'))
        tagi[link.text.strip()]= link.get('href')
    #print()

    #print("NXT BEZ TEKSTU... JESZCZE")

    nst_art_link = []
    for link in soup.find_all("a",{'title': 'Następny artykuł'} ):
        #print(link.get('href'))
        if not link.get('href') in nst_art_link:
            nst_art_link.append(link.get('href'))
            linki.append(link.get('href'))
    #print(nst_art_link)
    counter += 1

print(tagi)
print(tytuly)
print(leady)
print(linki)
