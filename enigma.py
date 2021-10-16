import binascii
import string
import random,sys
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
        if(self.wire[i] == len(self.char)-1):
            self.wire[i] = 0
        else:
            self.wire[i]=int(self.wire[i])+1

class Enigma():
    def __init__(self,rotors,ukw):
        self.rotors = rotors
        self.count = 0
        self.ukw = ukw
        self.chars = list(string.ascii_lowercase)

    def move(self):
        self.rotors[0].rotate()
        if(self.count%26 == 0):
            self.rotors[1].rotate()
        if(self.count %(26*26) == 0):
            self.rotors[1].rotate()
            self.rotors[2].rotate()
        self.count = self.count +1

    def reflect(self,a):
        firstval = self.round(a)
        a = self.chars[firstval]
        secondval = self.round(a,True)
        return self.chars[secondval]

    def round(self,a,isRev=False):
           min = 2 if isRev else 0
           max = -1 if isRev else 3
           step = -1 if isRev else 1
           a = self.chars.index(a)
           for i in range(min,max,step):
               a = self.rotors[i].wire[a]
               if (i==max-step):
                   #print("this might be erronoes: " + str(a))
                   a = self.ukw[a]
                   self.move()
                   return a
               if isRev:
                   #print("this might be erronoes: "+ str(a))
                   a = self.rotors[i-1].wire[a]
               else:
                   #print("this might be erronoes: " + str(a))
                   a = self.rotors[i+1].wire[a]

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
    rotorlist1 = [Rotor(rotor_I), Rotor(rotor_II), Rotor(rotor_III)]
    rotorlist2 = [Rotor(rotor_I),Rotor(rotor_II),Rotor(rotor_III)]

    enigma1 = Enigma(rotorlist1, ukw_a)
    enigma2 = Enigma(rotorlist1, ukw_a)
    print(enigma1.reflect("b"))
    #print(enigma1.reflect("j"))
    a = enigma1.reflect("m")
    print(a)
testrun()
main()