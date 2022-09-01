"""
ID: anudeep6
LANG: PYTHON2
TASK: namenum
"""
import numpy as np

fin = open('namenum.in', 'r')
fout = open('namenum.out', 'w')
n = int(fin.readline().strip())

okwords = open('dict.txt', 'r')
contents = okwords.read()
okwords = open('dict.txt', 'r')
oknames = []
for i in range(4617):
    name = okwords.readline().strip()
    oknames.append(name)

numtoletter = {2:['A', 'B', 'C'],
               3:['D', 'E', 'F'],
               4: ['G', 'H', 'I'],
               5: ['J', 'K', 'L'],
               6: ['M', 'N', 'O'],
               7: ['P', 'R', 'S'],
               8: ['T', 'U', 'V'],
               9: ['W', 'X', 'Y']}
names = []


def recuradd(curname, remnum):
    if remnum < 10:
        for letter in numtoletter[remnum]:
            if letter+curname not in contents:
                continue
            if letter+curname in oknames:
                names.append(letter+curname)
    else:
        num = remnum % 10
        for letter in numtoletter[num]:
            if letter+curname not in contents:
                continue
            recuradd(letter+curname, int(remnum/10))

recuradd('', n)
if len(names) == 0:
    fout.write('NONE' + '\n')
for name in sorted(names):
    fout.write(name + '\n')

fout.close()