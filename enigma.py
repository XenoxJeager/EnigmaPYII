import random
import string
import tkinter
from tkinter import ttk

from ttkthemes import *


def generatewire(lenght=26):
    a = []
    for i in range(0, lenght):
        a.append(i)
    random.shuffle(a)
    return a


def convert(a):
    wire = []
    for i in a:
        wire.append(string.ascii_letters.upper().index(i))
    return tuple(wire)


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


class Rotor():
    def __init__(self, wire, turn, char=None):
        self.char = char if char is not None else list(string.ascii_lowercase)
        self.wire = list(wire)
        self.turn = turn

    def rotate(self):
        char2 = []
        wire2 = []
        for i in range(0, len(self.char)):
            if (i == len(self.char) - 1):
                self.add(i)
                wire2.insert(0, self.wire[i])
                char2.insert(0, self.char[i])
            else:
                self.add(i)
                char2.insert(i + 1, self.char[i])
                wire2.insert(i + 1, self.wire[i])
        self.wire = wire2
        self.char = char2

    def add(self, i):
        if self.wire[i] == len(self.char) - 1:
            self.wire[i] = 0
        else:
            self.wire[i] = int(self.wire[i]) + 1


class Enigma():
    def __init__(self, rotors, ukw):
        self.rotors = rotors
        self.count = 0
        self.ukw = ukw
        self.chars = list(string.ascii_lowercase)
        self.plugboard = list(string.ascii_lowercase)

    def setplugboard(self, l):
        if len(l) == 26:
            self.plugboard = l

    def setpos(self, i, rotor):
        for l in range(0, i, 1):
            self.rotors[rotor].rotate()
            self.count = self.count + 1

    def rotate(self, rot0=0, rot1=0, rot2=0):
        self.setpos(rot0, 0)
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

    def reflect(self, a):
        firstval = self.forward(a)
        a = self.chars[firstval]
        secondval = self.backward(a)
        self.move()
        return secondval

    def backward(self, a):
        a = self.chars.index(a)
        for i in range(2, -1, -1):
            a = self.rotors[i].wire.index(a)
            if i == 0:
                return self.plugboard[a]

    def forward(self, a):
        a = self.plugboard.index(a)  # a = 0
        for i in range(0, 3, 1):
            a = self.rotors[i].wire[a]  # e=4
            if (i == 2):
                a = self.ukw[a]
                return a


def parserot(box):
    if box.get() == "I":
        rot = Rotor(rotor_I, pol_I)
    elif box.get() == "II":
        rot = Rotor(rotor_II, pol_II)
    elif box.get() == "III":
        rot = Rotor(rotor_III, pol_III)
    elif box.get() == "VI":
        rot = Rotor(rotor_IV, pol_IV)
    elif box.get() == "V":
        rot = Rotor(rotor_V, pol_V)
    return rot


def ukwparse():
    if ukw.get() == "ukw_a":
        return ukw_a
    elif ukw.get() == "ukw_b":
        return ukw_b
    elif ukw.get() == "ukw_c":
        return ukw_c


def boardparse():
    pboard = list(string.ascii_lowercase)
    try:
        a = text_map.get().split(" ")
        for i in a:
            try:
                pair = i.split(":")
                pboard[pboard.index(pair[0])] = pair[0]
                pboard[pboard.index(pair[1])] = pair[1]
            except:
                return pboard
        return pboard
    except:
        return pboard


def run():
    rotorlist1 = [parserot(val_1), parserot(val_2), parserot(val_3)]
    enigma = Enigma(rotorlist1, ukwparse())
    enigma.rotate(int(set1.get()), int(set2.get()), int(set3.get()))
    b = ""
    enigma.setplugboard(boardparse())
    out_map.delete('1.0', 'end-1c')

    for i in text_write.get("1.0", 'end-1c').lower():
        try:

            list(string.ascii_lowercase).index(i)
            b = b + enigma.reflect(i)
        except:
            print("a")
            b = "invalid input" + i
            break
    out_map.insert("end-1c", b)


def graphics():
    global val_1, val_2, val_3, ukw, text_write, text_map, out_map, set1, set2, set3
    window = ThemedTk(theme="arc")
    window.title = "Enigma"

    box_frame1 = tkinter.Frame(window, bd=1, padx=10, pady=5)
    box_frame2 = tkinter.Frame(window, bd=1, padx=10, pady=5)
    box_frame3 = tkinter.Frame(window, bd=1, padx=10, pady=5)
    box_frame4 = tkinter.Frame(window, bd=1, padx=10, pady=5)
    board_frame = tkinter.Frame(window, bd=1, padx=10, pady=5)
    encrypt_row = tkinter.Frame(window, bd=1, padx=10, pady=5)
    out_row = tkinter.Frame(window, bd=1, padx=10, pady=5)
    last_row = tkinter.Frame(window, bd=1, padx=10, pady=5)

    box_frame1.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    box_frame2.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
    box_frame3.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
    box_frame4.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
    encrypt_row.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)
    out_row.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)
    board_frame.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
    last_row.grid(row=6, column=0, sticky="nsew", padx=2, pady=2)

    val_1 = ttk.Combobox(box_frame1, values=["I", "II", "III", "IV", "V"], state="readonly")
    val_2 = ttk.Combobox(box_frame2, values=["I", "II", "III", "IV", "V"], state="readonly")
    val_3 = ttk.Combobox(box_frame3, values=["I", "II", "III", "IV", "V"], state="readonly")
    ukw = ttk.Combobox(box_frame4, values=["ukw_a", "ukw_b", "ukw_c"], state="readonly")

    val_1.set("I")
    val_2.set("II")
    val_3.set("III")
    ukw.set("ukw_a")
    val_1.pack(side="left", fill="x")
    val_2.pack(side="left", fill="y")
    val_3.pack(side="left", fill="y")
    ukw.pack(side="left", fill="y")

    ttk.Label(box_frame1, text="rotor 1").pack(side="left", fill="y", padx=10, pady=5)
    ttk.Label(box_frame2, text="rotor 2").pack(side="left", fill="y", padx=10, pady=5)
    ttk.Label(box_frame3, text="rotor 3").pack(side="left", fill="y", padx=10, pady=5)
    ttk.Label(box_frame4, text="ukw    ").pack(side="left", fill="y", padx=10, pady=5)
    ttk.Label(box_frame1, text="plugboard").pack(side="left", fill="y", padx=10, pady=5)
    ttk.Label(box_frame2, text="rotorpos").pack(side="left", fill="y", padx=10, pady=5)

    my_var = tkinter.StringVar(window)
    my_var.set("0")
    my_var2 = tkinter.StringVar(window)
    my_var2.set("0")
    my_var3 = tkinter.StringVar(window)
    my_var3.set("0")

    set1 = ttk.Spinbox(box_frame2, from_=0, to=26, width=3, state="readonly", textvariable=my_var)
    set2 = ttk.Spinbox(box_frame2, from_=0, to=26, width=3, state="readonly", textvariable=my_var2)
    set3 = ttk.Spinbox(box_frame2, from_=0, to=26, width=3, state="readonly", textvariable=my_var3)
    set1.pack(side="left", fill="y")
    set2.pack(side="left", fill="y")
    set3.pack(side="left", fill="y")

    my_var4 = tkinter.StringVar(window)
    my_var4.set("a:b c:d e:f")
    text_map = ttk.Entry(box_frame1,textvariable=my_var4)
    text_map.pack(side="left", fill="y", padx=10, pady=5)

    s1 = ttk.Scrollbar(encrypt_row)
    text_write = tkinter.Text(encrypt_row, height=4, width=50)
    s1.pack(side="left", fill="y")
    text_write.pack(side="left", fill="y")
    s1.config(command=text_write.yview)
    text_write.config(yscrollcommand=s1.set)

    s2 = ttk.Scrollbar(out_row)
    out_map = tkinter.Text(out_row, height=4, width=50)
    s2.pack(side="left", fill="y")
    out_map.pack(side="left", fill="y")
    s2.config(command=out_map.yview)
    out_map.config(yscrollcommand=s2.set)

    ttk.Button(last_row, text="encrypt", command=run).pack(side="left", fill="y")

    window.mainloop()


graphics()
