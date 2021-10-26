import random,string,tkinter
from tkinter import  ttk
from EnigmaPYII.package.rotor import Rotor
from ttkthemes import *

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
pol_I = 17
pol_II = 5
pol_III = 22
pol_IV = 10
pol_V = 26

rotor_I = convert("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
rotor_II = convert("AJDKSIRUXBLHWTMCQGZNPYFVOE")
rotor_III = convert("BDFHJLCPRTXVZNYEIWGAKMUSQO")
rotor_IV = convert("ESOVPZJAYQUIRHXLNFTGKDCMWB")
rotor_V = convert("VZBRGITYUPSDNHLXAWMJQOFECK")
ukw_a = convert("EJMZALYXVBWFCRQUONTSPIKHGD")
ukw_b = convert("YRUHQSLDPXNGOKMIEBFZCWVJAT")
ukw_c = convert("FVPJIAOYEDRZXWGCTKUQSBNMHL")
class Enigma():
    def __init__(self,rotors,ukw):
        self.rotors = rotors
        self.count = 0
        self.ukw = ukw
        self.chars = list(string.ascii_lowercase)
        self.plugboard = list(string.ascii_lowercase)

    def setplugboard(self,l):
        if len(l) == 26:
            self.plugboard = l

    def setpos(self,i,rotor):
        for l in range(0,i,1):
            self.rotors[rotor].rotate()
            self.count = self.count + 1

    def rotate(self,rot0=0,rot1=0,rot2=0):
        self.setpos(rot0,0)
        self.setpos(rot1, 1)
        self.setpos(rot2, 2)

    def move(self):
        self.rotors[0].rotate()
        if self.count % self.rotors[1].turn == 0:
            self.rotors[1].rotate()
        if self.count % (self.rotors[1].turn * self.rotors[1].turn) == 0:
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
                return self.plugboard[a]

    def forward(self,a):
           a = self.plugboard.index(a) # a = 0
           for i in range(0,3,1):
               a = self.rotors[i].wire[a] # e=4
               if (i==2):
                    a = self.ukw[a]
                    return a
                #print("this might be erronoes: " + str(a))

def main():
    while True:
        rotorlist1 = [Rotor(rotor_I,pol_I), Rotor(rotor_II,pol_II), Rotor(rotor_III,pol_III)]
        enigma2 = Enigma(rotorlist1, ukw_a)
        b = enigma2.chars.index("g")
        b2 = enigma2.chars.index("x")
        a = list(string.ascii_lowercase)
        a[b] = "x"
        a[b2] = "g"
        enigma2.setplugboard(a)
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

def graphics():
    window = ThemedTk(theme="arc")
    global val_1,val_2,val_3,ukw,text_write,text_map

    val_1 = ttk.Combobox(window,values=["I","II","III","IV","V"],state="readonly").grid(row=0,column=1,pady=10,padx=10,sticky = tkinter.N)
    val_2 = ttk.Combobox(window, values=["I", "II", "III", "IV", "V"], state="readonly").grid(row=1, column=1, pady=10,padx=10,sticky = tkinter.N)
    val_3 = ttk.Combobox(window, values=["I", "II", "III", "IV", "V"], state="readonly").grid(row=2, column=1, pady=10,padx=10,sticky = tkinter.N)
    ukw = ttk.Combobox(window, values=["ukw_1", "ukw_2", "ukw_3"], state="readonly").grid(row=3, column=1, pady=10,padx=10,sticky = tkinter.N)

    text_write = ttk.Entry(window,text="input...").grid(row=0,column=3,padx=10,pady=10,ipady=40,ipadx=70 ,sticky = tkinter.N)
    text_map = ttk.Entry(window, text="out").insert(window,"j")

    ttk.Label(window, text="rotor 1").grid(row=0,column=0,pady=10,padx=10,sticky = tkinter.N)
    ttk.Label(window, text="ukw").grid(row=3, column=0, pady=10, padx=10,sticky = tkinter.N)
    ttk.Label(window, text="rotor 2").grid(row=1,column=0,pady=10,padx=10,sticky = tkinter.N)
    ttk.Label(window, text="rotor 3").grid(row=2,column=0,pady=10,padx=10,sticky = tkinter.N)
    ttk.Button(window, text="encrypt",).grid(row=4,column=0,pady=10,padx=10,sticky = tkinter.N)
    window.mainloop()
#testrun()
#main()
graphics()



