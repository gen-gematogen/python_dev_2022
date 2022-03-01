import sys
import os
import urllib.request
import __init__ as init

if os.path.isfile(sys.argv[1]):
    with open(sys.argv[1]) as w:
        words = w.read().split()
else:
    with urllib.request.urlopen(sys.argv[1]) as w:
        words = w.read().decode().split()
    
try:
    size = int(sys.argv[2])
except:
    size = 5

words = [i for i in words if len(i) == size]
print(words)

print(init.gameplay(init.ask, init.inform, words))

