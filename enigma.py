import binascii
import string
import random
from typing import Optional

def generatewire(lenght=26):
    a =[]
    for i in range(0,lenght):
        a.append(i)
    random.shuffle(a)
    return a

def converter(a):
    l = []
    for i in a:
        l.append(list(string.ascii_letters).index(a))


class Rotor():
    wire: Optional[list]
    char: Optional[list]
    def __init__(self,wire,char=None):
        self.char = char if char is not None else list(string.ascii_lowercase)
        self.wire = wire
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
    def reverse(self):

class Enigma():
    def __init__(self,rotors):
        self.rotors = rotors
        self.count = 0
        self.resset = list(string.ascii_lowercase)

    def move(self):
        self.rotors[0].rotate()
        if(self.count%26 == 0):
            self.rotors[1].rotate()
        if(self.count %(26*26) == 0):
            self.rotors[1].rotate()
            self.rotors[2].rotate()
        self.count = self.count +1

    def decript(self,a):
        a = self.resset.index(a)
        for i in range(3,0,-1):
          a = self.rotors[i].wire.index(a)
          a = self.rotors[i].wire[a]
        return a
    def reflect(self,a):
        firstval = self.round(a)
        secondval = self.round(firstval,True)

    def testrun(self):
        a = self.resset.index("a")
        out =self.rotors[0].wire[a]
        print(out)
        self.move()
        a = self.resset.index("a")
        out = self.rotors[0].wire[a]
        print(out)
        self.move()

    def round(self,a,isRev=False):
           min = 2 if isRev else 0
           max = -1 if isRev else 3
           step = -1 if isRev else 1
           a = self.resset.index(a)
           print(*self.rotors[0].wire)
           for i in range(min,max,step):
               a = self.rotors[i].wire[a]
               if (i==max-step):
                   #print("this might be erronoes: " + str(a))
                   a = self.resset[a]
                   self.move()
                   return a
               if isRev:
                   #print("this might be erronoes: "+ str(a))
                   a = self.rotors[i-1].wire[a]
               else:
                   #print("this might be erronoes: " + str(a))
                   a = self.rotors[i+1].wire[a]

def main():
    rotorlist1 = []
    rotorlist2 = []
    for i in range(0,3):
        wire = generatewire()
        rotorlist1.append(Rotor(wire))
        rotorlist2.append(Rotor(wire))
    enigma = Enigma(rotorlist1)
