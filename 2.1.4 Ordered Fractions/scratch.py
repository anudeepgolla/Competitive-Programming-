"""
ID: anudeep6
LANG: PYTHON3
TASK: frac1
"""

fin = open('frac1.in', 'r')
fout = open('frac1.out', 'w')
n = int(fin.readline().strip())

def relprime(x,y):
    minim = min(x,y)
    for i in range(2,minim+1):
        if x % i == 0 and y % i == 0:
            return False
    return True

fractions = []
values = []
count = 0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if relprime(i,j):
            fractions.append((i,j))
            values.append((i/j, count))
            count += 1

fout.write('0/1' + '\n')
for value in sorted(values):
    fout.write(str(fractions[value[1]][0]) + '/' + str(fractions[value[1]][1]) + '\n')
fout.write('1/1' + '\n')
fout.close()