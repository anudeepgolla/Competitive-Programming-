"""
ID: anudeep6
LANG: PYTHON2
TASK: beads
"""
fin = open('beads.in', 'r')
fout = open('beads.out', 'w')
n = int(fin.readline().strip())
necklace = fin.readline().strip()
length = len(necklace)
maxcount = 0
for i in range(length):
    print(i)
    rightcount = 0
    leftcount = 0
    curright = i
    curleft = (i-1) % length
    rightletter = 'w'
    leftletter = 'w'
    for j in range(length):
        if necklace[(i+j)%length] != 'w':
            rightletter = necklace[(i+j)%length]
            break
    for j in range(length):
        if necklace[(i - j - 1) % length] != 'w':
            leftletter = necklace[(i - j - 1) % length]
            break
    print(leftletter)
    while (necklace[curright] == rightletter or necklace[curright] == 'w') and rightcount < length:
        rightcount += 1
        curright = (curright+1) % length
    while (necklace[curleft] == leftletter or necklace[curleft] == 'w') and leftcount < length:
        leftcount += 1
        curleft = (curleft-1) % length
    if (curright-curleft) > 0:
        excess = curright-curleft
    if (rightcount + leftcount) > maxcount:
        maxcount = rightcount + leftcount
    print('maxcount', leftcount, rightcount)
count = maxcount
if maxcount > length:
    count = length
fout.write(str(count) + '\n')
fout.close()
