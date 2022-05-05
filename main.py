from tkinter import N


num=input()
num=num.split()
n=num[0]
n=int(n)
k=num[1]
k=int(k)

import math

wynik = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
wynik = int(wynik)
print(wynik)