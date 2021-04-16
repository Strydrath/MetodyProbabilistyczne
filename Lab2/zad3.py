from peachpy import *
from peachpy.x86_64 import *

przedzialy = [0]*10

def zamien(liczba):
    potega = 30
    x = 0
    for j in range(31):
        x += liczba[j] * 2 ** potega
        potega -= 1
    return x


def generator():
    global przedzialy
    liczba = [0]*31
    liczba[0] = 1
    liczba[3] = 1
    liczba[5] = 1
    liczba[6] = 1
    p = 7
    q = 3
    m = 31
    for i in range(100000):
        for j in range (7,31):
            if liczba[j-p] != liczba[j-q]:
                liczba[j] = 1
            else:
                liczba[j] = 0
        x = zamien(liczba)
        #print(x)
        j = x*10//(2**m)
        przedzialy[j] += 1
        for j in range(7):
            liczba[j] = liczba[30-(7-j)]


generator()
for a in przedzialy:
    print(a)