# Sortowanie i lączenie list
#wpisujemy po spacji slowa i wypluwa liste bez duplikatow

def sort_str(a):
    lista = a.split(" ")
#    print(",".join(sorted(lista)))
    lista1 = set(lista)
    lista = list(lista1)
    lista.sort()
    print(" ".join(lista))

a = input("Wpisz słowa po spacji: ")
#a = input("Wpisz słowa rozdzielone przecinkiem: ").split(",")
sort_str(a)

#### krotsze

s = input()
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))
