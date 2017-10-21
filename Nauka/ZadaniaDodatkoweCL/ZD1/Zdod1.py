import random

a = "tekst tekst tekst"
b = ""

for i in a:
    x = random.randint(0,1)
    if x == 0:
        b += i.lower()
    else:
        b += i.upper()

print(b)
