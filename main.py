num=input()
num=num.split()
n=num[0]
n=int(n)
k=num[1]
k=int(k)

import math
def newton(n, k): 
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
print(newton (n, k))