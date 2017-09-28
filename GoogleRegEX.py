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
