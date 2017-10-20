#Factorial danej liczby
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input("Wpisz liczbę: "))
print (fact(x))
