"""
ID: anudeep6
LANG: PYTHON2
TASK: pprime
"""
import numpy as np

fin = open('pprime.in', 'r')
fout = open('pprime.out', 'w')
line = fin.readline().strip().split()
x = int(line[0])
atemp = x
y = int(line[1])
btemp = y

mindig = 0
while(atemp):
    mindig += 1
    atemp = int(atemp/10)
maxdig = 0
while(btemp):
    maxdig += 1
    btemp = int(btemp/10)

primes = []

def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def palindrome(n):
    digits= []
    while(n):
        digits.append(n%10)
        n = int(n/10)
    return digits == digits[::-1]


if 1 >= mindig and 1 <= maxdig:
    for a in range(1,10):
        if x <= a <= y and prime(a):
            primes.append(a)

if 2 >= mindig and 2 <= maxdig:
    for a in range(1,10):
        num = 11*a
        if x <= num <= y and prime(num):
            primes.append(num)

if 3 >= mindig and 3 <= maxdig:
    for a in range(1,10):
        for b in range(0,10):
            num = 100*a + 10*b + a
            if x <= num <= y and prime(num):
                primes.append(num)

if 4 >= mindig and 4 <= maxdig:
    for a in range(1,10):
        for b in range(0,10):
            num = 1000*a + 100*b + 10*b + a
            if x <= num <= y and prime(num):
                primes.append(num)

if 5 >= mindig and 5 <= maxdig:
    for a in range(1,10):
        for b in range(0,10):
            for c in range(0,10):
                num = 10000*a + 1000*b + 100*c + 10*b + a
                if x <= num <= y and prime(num):
                    primes.append(num)

if 6 >= mindig and 6 <= maxdig:
    for a in range(1,10):
        for b in range(0,10):
            for c in range(0,10):
                num = 100000*a + 10000*b + 1000*c + 100*c + 10*b + a
                if x <= num <= y and prime(num):
                    primes.append(num)

if 7 >= mindig and 7 <= maxdig:
    for a in range(1,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    num = 1000000*a + 100000*b + 10000*c + 1000*d + 100*c + 10*b + a
                    if x <= num <= y and prime(num):
                        primes.append(num)

if 8 >= mindig and 8 <= maxdig:
    for a in range(1,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    num = 10000000*a + 1000000*b + 100000*c + 10000*d + 1000*d + 100*c + 10*b + a
                    if x <= num <= y and prime(num):
                        primes.append(num)

'''
for i in range(x, 10**mindig):
    if palindrome(i) and prime(i):
        primes.append(i)

for i in range(10**(maxdig-1), y+1):
    if palindrome(i) and prime(i):
        primes.append(i)
'''

for i in sorted(primes):
    fout.write(str(i) + '\n')


fout.close()
