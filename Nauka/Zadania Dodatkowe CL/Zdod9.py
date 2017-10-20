def wypis(licz1,licz2):
    return """liczba {} mieści się w liczbie {} 
    {} razy
    {} to reszta z dzielenia""".format(licz2, licz1, licz1//licz2, licz1%licz2)

print(wypis(2,4))
print(wypis(8,4))
print(wypis(5,4))

