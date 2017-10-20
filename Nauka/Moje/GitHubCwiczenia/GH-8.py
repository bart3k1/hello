# Sortowanie i lączenie list

def sort_str(a):
    lista = a.split(",")
#    print(",".join(sorted(lista)))
    lista.sort()
    print(",".join(lista))

a = input("Wpisz słowa po przecinku: ")
#a = input("Wpisz słowa rozdzielone przecinkiem: ").split(",")
sort_str(a)
