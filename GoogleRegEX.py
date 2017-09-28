import re
def find(pat, text):
    match = re.search(pat, text)
    if match: print(match.group())
    else: print('Not found')

find('iig', 'piiig')
find('..g', 'piiig')
find('..gs', 'piiig albo cos jak xyzgs')
find('.\...g', 'p.iig or xyzgs')
find(r'.\...g', 'p.iig or xyzgs')
find(r':\w\w\w', 'blah :cat blah blah')
# \w word character a-z 0-9
find(r':\d\d\d', 'blah :123')
# \d digits
find(r':\s\d\s\d\s\d', 'blah : 1 2 3')
# \s space
find(r':\s\d\s+\d\s\d', 'blah : 1     2 3')
# + 1 or more
find(r':.+', 'blah blah :kitten blah blah')
find(r':\w+', 'blah blah :kitten123@')
# \S not space character
find(r':\S+', 'blah blah :kitten123@ aaa')
# emaile
find(r'\w+@\w+', 'blah blah bart.weg@gmail.com blah 123')
#sety characterow
find(r'[\w.]+@[\w.]+', 'blah blah bart.weg@gmail.com blah 123')
find(r'[\w.]+@[\w.]+', 'blah blah .bart.weg@gmail.com blah 123')
find(r'\w[\w.]+@[\w.]+', 'blah blah .bart.weg@gmail.com blah 123')
print()
print('Nowy wzór:')
def find_N(pat, text):
    match = re.search(pat, text)
    if match: print(match.group(1), match.group(2))
    else: print('Not found')

#Separately group (1), (2) ...
find_N(r'([\w.]+)@([\w.]+)', 'blah blah bart.weg@gmail.com blah 123')

print()
print('Nowy wzór: FINDALL')
def find_A(pat, text):
    match = re.findall(pat, text)
    if match: print(match) #zmiana bo nie grupa
    else: print('Not found')


find_A(r'[\w.]+@[\w.]+', 'blah blah bart.weg@gmail.com blah 123 bart3k1@gmail.com lskdja jdas bart.3k1@gmail.com')
find_A(r'([\w.]+)@([\w.]+)', 'blah blah bart.weg@gmail.com blah 123 bart3k1@gmail.com lskdja jdas bart.3k1@gmail.com')

#optional arguments... nie dziala
find_A(r'([\w.]+)@([\w.]+)', 'blah blah bart.weg@gmail.com blah 123 bart3k1@gmail.com', re.IGNORECASE())
