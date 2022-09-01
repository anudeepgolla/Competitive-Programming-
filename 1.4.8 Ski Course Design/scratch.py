"""
ID: anudeep6
LANG: PYTHON2
TASK: skidesign
"""
import numpy as np

fin = open('skidesign.in', 'r')
fout = open('skidesign.out', 'w')
n = int(fin.readline().strip())
hills = []
for i in range(n):
    hills.append(int(fin.readline().strip()))

hills = sorted(hills)
min = hills[0]
max = hills[len(hills)-1]

def calculate(lower, upper, nums):
    total = 0
    for num in nums:
        if num >= lower and num <= upper:
            continue
        elif num < lower:
            total += ((lower - num)**2)
        elif num > upper:
            total += ((num - upper) ** 2)
    return total

mintotal = 1000000000
bottom = min
top = min +17
while top <= max:
    curtotal = calculate(bottom, top, hills)
    if curtotal < mintotal:
        mintotal = curtotal
    bottom += 1
    top += 1

'''
dist = max - min - 17
half = int(dist/2)
if dist % 2 == 0:
    result = 2 * (half ** 2)
    hills[0] += half
    hills[len(hills) - 1] -= half
else:
    result = ((half ** 2) + ((half + 1) ** 2))
    hills[0] += (half)
    hills[len(hills) - 1] -= (half + 1)


total = 0
while range > 17:
    result = 0
    dist = range - 17
    half = int(dist/2)
    if dist % 2 == 0:
        result = 2*(half**2)
        hills[0] += half
        hills[len(hills) - 1] -= half
    else:
        result = ((half ** 2) + ((half + 1) ** 2))
        hills[0] += (half)
        hills[len(hills) - 1] -= (half+1)
    total += result
    hills = sorted(hills)
    min = hills[0]
    max = hills[len(hills)-1]
    range = max - min
    print(hills)
'''

fout.write(str(mintotal) + '\n')
fout.close()