#BINARY - jesli jest stringiem mozna zamienic w decimala: int(i,2)
#wprowadzic binarne w input i dostajemy podzielne przez 5
value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp % 5:
        value.append(p)

print (','.join(value))
