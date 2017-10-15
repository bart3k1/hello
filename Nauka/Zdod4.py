#SZYFR CEZARA ROT13
#DEKODER
import string

lc = string.ascii_lowercase
uc = string.ascii_uppercase

#for i in lc:
#    print(i, lc.index(i), lc[(int((lc.index(i))) + 13) % 26 ])
#for i in uc:
#    print(i, uc.index(i), uc[(int((uc.index(i))) + 13) % 26 ])

def rot13(string_in):
    string_out = ""
    for i in string_in:
        if i in lc:
            string_out += lc[(int((lc.index(i))) + 13) % 26 ]
#
        elif i in uc:
            string_out += uc[(int((uc.index(i))) + 13) % 26 ]
        else:
            string_out += i
    print(string_out)

rot13("GrF .,.,sg")
