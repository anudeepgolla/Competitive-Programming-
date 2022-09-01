"""
ID: anudeep6
LANG: PYTHON3
TASK: nocows
"""


fin = open('nocows.in', 'r')
fout = open('nocows.out', 'w')

line = fin.readline().strip().split()
N = int(line[0])
K = int(line[1])

ways = [[0 for i in range(K)] for j in range(N)]
subtrees = [[0 for i in range(K)] for j in range(N)]
for i in range(K):
    subtrees[0][i] = 1
ways[0][0] = 1

#ways[4][2] = 2
#ways[6][2] = 1

#ij =




for x in range(2, N, 2):
    for y in range(1,K):
        for k in range(0,x,2):
            ways[x][y]+=ways[k][y-1] * ways[x-k-2][y-1]
            if y >= 2:
                ways[x][y]+=2*(ways[k][y-1] * subtrees[x-k-2][y-2])
        for i in range(y,K):
            subtrees[x][i] += ways[x][y]

print(subtrees)
print(ways)


'''
for x in range(2, N, 2):
    for y in range(1,K):
        for k in range(0,x,2):
            ways[x][y]+=ways[k][y - 1] * ways[x - k - 2][y - 1]
            ways[x][y]+=2*(sum(ways[k][y-1]*ways[x-k-2][y-i] for i in range(2,y+1)))
'''

fout.write(str(ways[N-1][K-1]%9901) + '\n')
fout.close()
