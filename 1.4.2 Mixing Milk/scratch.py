"""
ID: anudeep6
LANG: PYTHON2
TASK: milk
"""
import numpy as np

fin = open('milk.in', 'r')
fout = open('milk.out', 'w')
nums = fin.readline().strip().split()
n = int(nums[0])
m = int(nums[1])

milks = {}
for i in range(m):
    nums = fin.readline().strip().split()
    x = int(nums[0])
    y = int(nums[1])
    if x in milks:
        milks[x] += y
    else:
        milks[x] = y

curmilk = 0
curmoney = 0
for key in sorted(milks):
    if (curmilk + milks[key]) < n:
        curmilk += milks[key]
        curmoney += (milks[key]*key)
    else:
        curmoney += ((n-curmilk)*key)
        curmilk = n
        break

fout.write(str(curmoney) + '\n')
fout.close()
