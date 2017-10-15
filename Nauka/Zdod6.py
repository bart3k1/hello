def dzielnik(licz1,licz2):
    a = licz1
    b = licz2
    while b != 0:
        c = a%b
        a = b
        b = c

    #print("Największy wspólny dzielnik liczb: {} i {} to {}".format(licz1,licz2,a))
    return a
#dzielnik(192, 348)
#dzielnik(42, 56)
#dzielnik(84, 18)

