"""
ID: anudeep6
LANG: PYTHON3
TASK: money
"""


fin = open('money.in', 'r')
fout = open('money.out', 'w')

line = fin.readline().strip().split()
V=int(line[0])
N=int(line[1])
amts = []
while line:
    line = fin.readline().strip().split()
    for l in line:
        if l not in amts:
            amts.append(l)

arr = [0]*(N+1)
arr[0] = 1
for l in amts:
    num = int(l)
    for i in range(num, N+1):
        arr[i] += arr[i - num]
    print(arr)

fout.write(str(arr[-1]) + '\n')
fout.close()