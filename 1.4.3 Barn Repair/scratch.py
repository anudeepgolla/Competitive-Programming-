"""
ID: anudeep6
LANG: PYTHON2
TASK: barn1
"""
import numpy as np

fin = open('barn1.in', 'r')
fout = open('barn1.out', 'w')
nums = fin.readline().strip().split()
m = int(nums[0])
s = int(nums[1])
c = int(nums[2])
cows = []
dists = {}

for i in range(c):
    num = int(fin.readline().strip())
    cows.append(num)

sortedcows = sorted(cows)
prev = sortedcows[0]
for i in range(1,c):
    dists[i] = sortedcows[i] - prev
    prev = sortedcows[i]

if m == 1:
    space = sortedcows[len(sortedcows)-1] - sortedcows[0] + 1
elif m >= c:
    space = c
else:
    sorteddists = sorted(dists.items(), key=lambda item: item[1])
    parts = []
    for i in range(m-1):
        parts.append(sorteddists[len(sorteddists)-1-i][1])

    totpart = sum(parts[i] for i in range(len(parts)))
    space = sortedcows[len(sortedcows) - 1] - sortedcows[0] - totpart + m

#print(sorteddists)
#print(cows)
fout.write(str(space) + '\n')
fout.close()