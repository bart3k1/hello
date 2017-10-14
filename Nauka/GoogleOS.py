import sys
import os
# listujemy katalog i wypisujemy sciezki i sciezki bezwzgledne
def list(dir):
    filenames = os.listdir(dir)
    print(filenames)
    for filename in filenames:
        path = os.path.join(dir, filename)
        print(path)
        print(os.path.abspath(path))
def main():
    list(sys.argv[1])

#aktualny katalog
list('.')
list('../')
list('/tmp')

# exists
print(os.path.exists('/home'))
print(os.path.exists('/home/b'))
#print(os.mkdir('/home/b/a'))
print(os.mkdir('/home/b/b'))
print(os.path.exists('/home/b/a'))

#shutil

import shutil
shutil.copy('/home/b/a/1.txt', '/home/b/b/')
