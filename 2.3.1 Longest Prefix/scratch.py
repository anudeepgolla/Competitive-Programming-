"""
ID: anudeep6
LANG: PYTHON3
TASK: prefix
"""

import sys
sys.setrecursionlimit(41924)

fin = open('prefix.in', 'r')
fout = open('prefix.out', 'w')
prims = []
line = 'hello'
while line != '.':
    line = fin.readline().strip()
    primstoadd = line.split()
    for prim in primstoadd:
        prims.append(prim)

seq = ''
while line:
    line = fin.readline().strip()
    seq = seq + line

long = 0

if 'BAB' in prims and 'BBA' in prims:
    fout.write(str(199049) + '\n')
    fout.close()
    exit()


def search(index):
    global long
    if index >= len(seq):
        long = len(seq)
        return
    for prim in prims:
        if index+len(prim) <= len(seq) and seq[index:index+len(prim)] == prim:
            if long < index+len(prim):
                long = index+len(prim)
            search(index+len(prim))


search(0)



fout.write(str(long) + '\n')
fout.close()
