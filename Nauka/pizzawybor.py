from pizza import pizza
from pizza import skladniki

for i in sorted(skladniki):
    print(i)
x = "anchovies" #input("Wpisz składnik: ")

for k,v in pizza.items():
    if x in v:
        print(k,v)


