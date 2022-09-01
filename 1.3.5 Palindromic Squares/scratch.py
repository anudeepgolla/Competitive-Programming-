"""
ID: anudeep6
LANG: PYTHON2
TASK: palsquare
"""
import numpy as np

fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')
n = int(fin.readline().strip())

letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K'}

def convertfrom(num, b):
    i = 0
    sum = 0
    while num:
        sum += ((num % 10)*np.power(b, i))
        i += 1
        num = int(num/10)
    return sum

def convertto(num, b):
    digits = []
    while num:
        rem = str(num % b)
        if int(rem) > 9:
            rem = letters[int(rem)]
        digits.append(rem)
        num = int(num / b)
    return ''.join(digits[::-1])

def isPalindrome(num):
    strnum = str(num)
    halflen = int((len(strnum))/2)
    if (len(strnum) % 2) == 0:
        return strnum[:halflen] == strnum[halflen:][::-1]
    else:
        return strnum[:halflen] == strnum[halflen+1:][::-1]


for i in range(1, 301):
    result = convertto(i**2, n)
    if isPalindrome(result):
        fout.write(convertto(i, n) + ' ' + str(result) + '\n')
fout.close()
