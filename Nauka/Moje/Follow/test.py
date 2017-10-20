a = "http://dziendobry.tvn.pl/wideo,2064,n/maseczka-z-jarzebiny-spektakularny-efekt-juz-po-10-dniach,242129.html"
b = a[24:]
print(b)

f = open('out.txt', 'w')
print >> f, 'Filename:', filename  # or f.write('...\n')
f.close()
