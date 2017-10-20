#wpisujemy numery przy uzyciu klawiatury telefonu
lista = [[["0"],[" "]],
 [["1"],[".","!","?"]],
 [['2'],['a','b','c']],
 [['3'],['d','e','f']],
 [['4'],['g','h','i']],
 [['5'],['j','k','l']],
 [['6'],['m','n','o']],
 [['7'],['p','q','r', 's']],
 [['8'],['t','u','v']],
 [['9'],['w','x','y', 'z']]
  ]

def ile_cyfr(x):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if x in lista[i][j]:
                return((lista[i][0]) * (lista[i][j].index(x)+1))

for i in input("Wpisz: "):
    print("".join(ile_cyfr(i)), end ="")

