#PESEL PRZEZ STULECIA
def validate_pesel(l):
    iloczyn = []
    lista_wag = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    for i in range(len(l)-1):
        iloczyn.append(int(l[i])*lista_wag[i])
    #modulo sumy iloczynu odejmujemy od 10
    kontrola  = 10 - (sum(iloczyn) % 10)

    if kontrola == int(l[-1]):
        return "PESEL zgodny"
    else:
        return "PESEL jest błędny"

a = '78061505172'
b = '44051401358'
#c = input("Wpisz PESEL: ")
print(validate_pesel(str(a)))
print(validate_pesel(str(b)))
#print(validate_pesel(str(c)))

