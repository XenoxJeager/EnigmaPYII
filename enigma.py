import binascii
import string
import random,re
from typing import Optional

# i will add it to the other class
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
    return tuple(wire)

#variables
rotor_I = convert("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
rotor_II = convert("AJDKSIRUXBLHWTMCQGZNPYFVOE")
rotor_III = convert("BDFHJLCPRTXVZNYEIWGAKMUSQO")
rotor_IV = convert("ESOVPZJAYQUIRHXLNFTGKDCMWB")
rotor_V = convert("VZBRGITYUPSDNHLXAWMJQOFECK")
ukw_a = convert("EJMZALYXVBWFCRQUONTSPIKHGD")
ukw_b = convert("YRUHQSLDPXNGOKMIEBFZCWVJAT")
ukw_c = convert("FVPJIAOYEDRZXWGCTKUQSBNMHL")

class Rotor():
    wire: Optional[list]
    char: Optional[list]

    def __init__(self,wire,char=None):
        self.char = char if char is not None else list(string.ascii_lowercase)
        self.wire = list(wire)

    def rotate(self):
        char2 = []
        wire2 = []
        for i in range(0,len(self.char)):
            if (i == len(self.char)-1):
                self.add(i)
                wire2.insert(0,self.wire[i])
                char2.insert(0,self.char[i])
            else:
                self.add(i)
                char2.insert(i+1, self.char[i])
                wire2.insert(i+1, self.wire[i])
        self.wire = wire2
        self.char = char2
    def add(self,i):
        if self.wire[i] == len(self.char)-1:
            self.wire[i] = 0
        else:
            self.wire[i]=int(self.wire[i])+1

class Enigma():
    def __init__(self,rotors,ukw):
        self.rotors = rotors
        self.count = 0
        self.ukw = ukw
        self.chars = list(string.ascii_lowercase)

    def setter(self,i,rotor):
        for l in range(0,i,1):
            self.rotors[rotor].rotate()

    def rotate(self,rot0=0,rot1=0,rot2=0):
        self.setter(rot0,0)
        self.setter(rot1, 1)
        self.setter(rot2, 2)

    def move(self):
        self.rotors[0].rotate()
        if self.count % 26 == 0:
            self.rotors[1].rotate()
        if self.count % (26 * 26) == 0:
            self.rotors[1].rotate()
            self.rotors[2].rotate()
        self.count = self.count + 1

    def reflect(self,a):
        firstval = self.forward(a)
        a = self.chars[firstval]
        secondval = self.backward(a)
        self.move()
        return secondval

    def backward(self,a):
        a = self.chars.index(a)
        for i in range(2,-1,-1):
            a = self.rotors[i].wire.index(a)
            if i == 0:
                return self.chars[a]

    def forward(self,a):
           a = self.chars.index(a) # a = 0
           for i in range(0,3,1):
               a = self.rotors[i].wire[a] # e=4
               if (i==2):
                    a = self.ukw[a]
                    return a
                #print("this might be erronoes: " + str(a))

def testrun():
    letter = list(string.ascii_lowercase)
    letterrev = []
    for i in letter:
        rotorlist1 = [Rotor(rotor_I), Rotor(rotor_II), Rotor(rotor_III)]
        enigma1 = Enigma(rotorlist1, ukw_a)
        letterrev.append(enigma1.reflect(i))
    print(*letter)
    print(*letterrev)

def main():
    while True:
        rotorlist1 = [Rotor(rotor_I), Rotor(rotor_II), Rotor(rotor_III)]
        enigma2 = Enigma(rotorlist1, ukw_a)
        enigma2.rotate(1,8,9)
        a = input("enigma>")
        b = ""
        for i in a.lower():
            try:
                list(string.ascii_lowercase).index(i)
                b = b + enigma2.reflect(i)
            except:
                b="invalid input"
                break
        print("out>" + b)

#testrun()
main()




