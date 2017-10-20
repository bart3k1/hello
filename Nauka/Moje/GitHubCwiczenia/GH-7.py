d = input("Podaj dwie liczby oddzielone przecinkiem: ").split(",")
#Zmieniamy na inty:
d_int = [int(x) for x in d]
print (d_int)
l = []
for i in range(d_int[0]):
    l.append([])
    for j in range(d_int[1]):
        l[i].append(j*i)


print(l)




