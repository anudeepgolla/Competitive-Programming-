"""
ID: anudeep6
LANG: PYTHON2
TASK: sprime
"""
import numpy as np

fin = open('sprime.in', 'r')
fout = open('sprime.out', 'w')
n = int(fin.readline().strip())


def prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

superprimes = [2,3,5,7]
tempsuperprimes = []
for i in range(n-1):
    for sp in superprimes:
        for j in [1,3,7,9]:
            num = 10*sp + j
            if prime(num):
                tempsuperprimes.append(num)
    superprimes = [x for x in tempsuperprimes]
    tempsuperprimes = []
'''
def superprime(n):
    while(n):
        if n in superprimes:
            return True
        if not prime(n):
            return False
        n = int(n/10)
    return True

superprimes = set()

for i in range(10**(n-1), 10**n):
    print(i)
    if superprime(i):
        superprimes.append(i)
'''
for i in sorted(superprimes):
    fout.write(str(i) + '\n')
fout.close()
