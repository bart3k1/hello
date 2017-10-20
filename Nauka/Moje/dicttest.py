fon = {}
fon['a'] = 123
fon['b'] = 456

print(fon)
print(fon.items())
print(fon.keys())
print(fon.values())
for k,v in fon.items():
    print(k,fon[k],v)
