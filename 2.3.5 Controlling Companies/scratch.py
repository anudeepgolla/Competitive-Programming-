"""
ID: anudeep6
LANG: PYTHON3
TASK: concom
"""


fin = open('concom.in', 'r')
fout = open('concom.out', 'w')

N = int(fin.readline().strip())
owns = [[0 for i in range(101)] for j in range(101)]
controls = [[0 for i in range(101)] for j in range(101)]
for i in range(101):
    controls[i][i] = 1

def addcontroller(x,y):
    if not controls[x][y]:
        controls[x][y] = 1
        for j in range(1,101):
            owns[x][j] += owns[y][j]
        for j in range(1,101):
            if controls[j][x]:
                addcontroller(j,y)
        for j in range(1,101):
            if owns[x][j] > 50:
                addcontroller(x,j)


def addowner(x,y,z):
    for i in range(1,101):
        if controls[i][x]:
            owns[i][y] += z
    for i in range(1,101):
        if owns[i][y] > 50:
            addcontroller(i,y)

for i in range(N):
    line = fin.readline().strip().split()
    addowner(int(line[0]), int(line[1]), int(line[2]))
    '''
    owns[int(line[0])][int(line[1])] = int(line[2])
    if int(line[2]) > 50:
        controls[int(line[0])][int(line[1])] = 100
        for num in range(1,101):
                    controls[int(line[0])][num] += owns[int(line[1])][num]
    for num in range(1, 101):
        if controls[num][int(line[0])] > 50:
                controls[num][int(line[1])] += int(line[2])
    '''


for row in owns:
    print(controls)

'''
for num in range(1, 101):
    if controls[int(line[1])][num] > 50:
        controls[int(line[0])][num] = 100
'''

for i in range(101):
    for j in range(101):
        if controls[i][j] and i != j:
            fout.write(str(i) + ' ' + str(j) + '\n')

fout.close()