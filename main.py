from tkinter import N


num=input()
num=num.split()
n=num[0]
n=int(n)
k=num[1]
k=int(k)

def silnia(x): return x*silnia(x-1) if x > 1 else 1

wynik = silnia(n)/(silnia(k)*silnia(n-k))
print(wynik)