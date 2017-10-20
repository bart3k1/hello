import math

c = 50
h = 30
d = input("Wpisz 3 liczby oddzielone przecinkiem: ").split(",")
s= []
for i in d:
	s.append(str(round(math.sqrt((2*c*float(i))/h))))
print(",".join(s))


#print(round(math.sqrt(x)))
