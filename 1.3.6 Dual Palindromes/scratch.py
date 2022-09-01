"""
ID: anudeep6
LANG: PYTHON2
TASK: dualpal
"""
import numpy as np

fin = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')
nums = fin.readline().strip().split()
n = int(nums[0])
s = int(nums[1])


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


listed = 0
start = s + 1
while listed < n:
    pals = 0
    for i in range(2,11):
        if isPalindrome(convertto(start, i)):
            pals += 1
        if pals >= 2:
            break
    if pals >= 2:
        fout.write(str(start) + '\n')
        listed += 1
    start += 1

fout.close()
