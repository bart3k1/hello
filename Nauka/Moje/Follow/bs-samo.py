from bs4 import BeautifulSoup

with open("http://www.py4inf.com/code/romeo.txt") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>data</html>")
