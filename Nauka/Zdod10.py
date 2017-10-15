def najkslowo(tekst):
    lista = tekst.split(" ")
    slowo = lista[0]
    for i in lista:
        if len(i) < len(slowo):
            slowo = i
    print(slowo)

najkslowo("Litwo ojczyzno moja Ja mam Ala ok j kkm pj")
