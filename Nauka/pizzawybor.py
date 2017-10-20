from _pizza import pizza
from _pizza import skladniki

for i in sorted(skladniki):
    print(i)
x = input("Wpisz składnik: ")

for k,v in pizza.items():
    if x in v:
        print(k,v)


