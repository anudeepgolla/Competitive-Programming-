"""
ID: anudeep6
LANG: PYTHON2
TASK: wormhole
"""
import numpy as np

fin = open('wormhole.in', 'r')
fout = open('wormhole.out', 'w')
n = int(fin.readline().strip())
holes = [[0 for i in range(2)]for j in range(n)]
levels = {}


for i in range(n):
    line = fin.readline().strip().split()
    holes[i][0] = int(line[0])
    holes[i][1] = int(line[1])
    if holes[i][1] in levels:
        levels[holes[i][1]].append(holes[i][0])
    else:
        levels[holes[i][1]] = [holes[i][0]]

for level in levels:
    levels[level] = sorted(levels[level])


def find(x,y):
    for i in range(n):
        if holes[i][0] == x and holes[i][1] == y:
            return i

def test(pairings):
    for key in pairings:
        '''
        current = key
        jump  = pairings[key]
        used = []
        yes = False
        for i in range(n):
            #print(i, key, current, jump, used)
            if current in used or jump in used:
                yes = True
                break
            else:
                used.append(current)
                used.append(jump)
                y = holes[jump][1]
                x = holes[jump][0]
                index = levels[y].index(x)
                if index == (len(levels[y]) - 1):
                    break
                else:
                    current  = find(levels[y][index+1],y)
                    jump = pairings[current]
        if yes:
            return True
            '''
        current = key
        for i in range(n):
            y = holes[pairings[current]][1]
            x = holes[pairings[current]][0]
            index = levels[y].index(x)
            if index == (len(levels[y]) - 1):
                break
            current = find(levels[y][index + 1], y)
        if i == (n-1):
            return True
    return False


pairs = {}
successful = 0

def pair():
    global successful
    first = -1
    for i in range(n):
        if i not in pairs:
            first = i
            break
    if first == -1:
        if test(pairs):
            print(pairs)
            successful += 1
    else:
        for j in range(first+1, n):
            if j not in pairs:
                pairs[j] = first
                pairs[first] = j
                pair()
                del pairs[j]
                del pairs[first]

pair()

fout.write(str(successful) + '\n')
fout.close()
