"""
ID: anudeep6
LANG: PYTHON2
TASK: gift1
"""
fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')
lines = fin.read().splitlines()
np = int(lines[0])
accounts = {}
names = ['a'] * np
for i in range(np):
    accounts[lines[i+1]] = 0
    names[i] = lines[i+1]
curline = np
for i in range(np):
    curline += 1
    name = lines[curline]
    curline += 1
    data = lines[curline].split()
    total, div = int(data[0]), int(data[1])
    accounts[name] -= total
    if div != 0:
        accounts[name] += (total % div)
    for j in range(div):
        curline += 1
        accounts[lines[curline]] += int(total/div)
for i in range(np):
    fout.write(names[i] + ' ' + str(accounts[names[i]]) + '\n')
fout.close()
