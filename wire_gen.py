import string
import random

def generatewire(lenght=26):
    a =[]
    for i in range(0,lenght):
        a.append(i)
    random.shuffle(a)
    return a

def convert(a):
    wire = []
    for i in a:
        wire.append(string.ascii_letters.upper().index(i))
    return wire