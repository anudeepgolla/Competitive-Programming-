"""
ID: anudeep6
LANG: PYTHON3
TASK: hamming
"""

fin = open('hamming.in', 'r')
fout = open('hamming.out', 'w')
line = fin.readline().strip().split()
N = int(line[0])
B = int(line[1])
D = int(line[2])

dists = {}
for i in range(2**B):
    for j in range(i+1, 2**B):
        distance = 0
        for k in range(B):
            if not((i & 1<<k and j & 1<<k) or (not(i & 1<<k or j & 1<<k))):
                distance+=1
        if distance >= D:
            if i not in dists:
                dists[i] = {j}
            else:
                dists[i].add(j)

numset = []
rem = N % 10
lines = int(N/10)

def check(newnum, oldset):
    for num in oldset:
        if num in dists and newnum not in dists[num]:
            return False
    return True

def search():
    print(numset)
    if len(numset) == N:
        #print(numset)
        newnumset = [str(x) for x in numset]
        for i in range(lines):
            fout.write(' '.join(newnumset[10 * i:10 * (i + 1)]) + '\n')
        if rem > 0:
            fout.write(' '.join(newnumset[N - rem:]) + '\n')
        fout.close()
        exit()
    if len(numset) == 0:
        start = -1
    else:
        start = numset[-1]
    for i in range(start+1,2**B):
        if check(i, numset):
            numset.append(i)
            search()
            numset.remove(i)

search()
