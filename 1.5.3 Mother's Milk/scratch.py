"""
ID: anudeep6
LANG: PYTHON2
TASK: milk3
"""
import numpy as np

fin = open('milk3.in', 'r')
fout = open('milk3.out', 'w')
line = fin.readline().strip().split()
A = int(line[0])
B = int(line[1])
C = int(line[2])

visited = np.zeros((A+1,B+1,C+1))
accept = []

def recur(a,b,c):
    if visited[a][b][c]:
        return
    visited[a][b][c] = 1
    if a == 0:
        accept.append((a,b,c))

    x = min(a, B-b)
    recur(a-x, b+x, c)
    x = min(A-a, b)
    recur(a + x, b - x, c)
    x = min(a, C - c)
    recur(a - x, b, c + x)
    x = min(A-a, c)
    recur(a + x, b, c - x)
    x = min(b, C - c)
    recur(a, b - x, c + x)
    x = min(B-b, c)
    recur(a, b + x, c - x)

recur(0,0,C)
accepts = []

for triple in accept:
    if triple not in accepts:
        accepts.append(triple[2])
saccepts = [str(x) for x in sorted(accepts)]
fout.write(' '.join(saccepts) + '\n')

fout.close()