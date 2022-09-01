"""
ID: anudeep6
LANG: PYTHON2
TASK: numtri
"""
import numpy as np

fin = open('numtri.in', 'r')
fout = open('numtri.out', 'w')
n = int(fin.readline().strip())
maxes = [[0 for i in range(n)] for j in range(n)]

x = int(fin.readline().strip())
maxes[0][0] = x

for i in range(n-1):
    row = [int(num) for num in fin.readline().strip().split()]
    maxes[i + 1][0] = maxes[i][0] + row[0]
    maxes[i + 1][i + 1] = maxes[i][i] + row[i+1]
    for j in range(1, i+1):
        maxes[i + 1][j] = max(maxes[i][j-1], maxes[i][j]) + row[j]

fout.write(str(max(maxes[n-1])) + '\n')

fout.close()
