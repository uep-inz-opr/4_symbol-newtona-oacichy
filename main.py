from tkinter import N


num=input()
num=num.split()
n=num[0]
n=int(n)
k=num[1]
k=int(k)

import math
def silnia(x): return x*silnia(x-1) if x > 1 else 1

wynik = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
print(wynik)