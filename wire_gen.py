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