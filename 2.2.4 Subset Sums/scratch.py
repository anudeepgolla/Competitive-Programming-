"""
ID: anudeep6
LANG: PYTHON3
TASK: subset
"""

fin = open('subset.in', 'r')
fout = open('subset.out', 'w')
n = int(fin.readline().strip())

half = n*(n+1)/4
inthalf = int(half)

sums = [0]*1000

if inthalf != half:
    fout.write('0\n')
    fout.close()
else:
    sums[0]=1
    sums[1]=1
    for i in range(2,n+1):
        prev = i-1
        tempsums = sums.copy()
        for j in range(i, i + int(prev*(prev+1)/2) + 1):
            tempsums[j] += sums[j-i]
            print(i,j)
        sums=tempsums
    fout.write(str(int(sums[inthalf]/2)) + '\n')
    fout.close()