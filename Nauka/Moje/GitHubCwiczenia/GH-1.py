# Wypisuje podzielne przez 7 ale nei przez 5 z zakresu 2000-3200
for i in range(2000, 3201):
    if i % 7 == 0:
        if i % 5 != 0:
            print(i, end=',')

    else:
        pass
print()

# 2 z listą
print("To samo z użyciem listy: ")
l = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        l.append(str(i))
print(",".join(l))
