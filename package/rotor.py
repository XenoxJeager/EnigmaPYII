import string
import random
class Rotor():
    def __init__(self,wire,turn,char=None):
        self.char = char if char is not None else list(string.ascii_lowercase)
        self.wire = list(wire)
        self.turn = turn

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
