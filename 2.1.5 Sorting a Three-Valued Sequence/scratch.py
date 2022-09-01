"""
ID: anudeep6
LANG: PYTHON3
TASK: sort3
"""

fin = open('sort3.in', 'r')
fout = open('sort3.out', 'w')
n = int(fin.readline().strip())
ones = 0
twos = 0
threes = 0
seq = []
for i in range(n):
    x = int(fin.readline().strip())
    seq.append(x)
    if x == 1:
        ones += 1
    elif x == 2:
        twos += 1
    else:
        threes += 1


wrongs = 0
twosinone=0
threesinone=0
onesintwo=0
threesintwo=0
onesinthree=0
twosinthree=0
swaps =0


for i in range(ones):
    if seq[i] == 2:
        wrongs+=1
        twosinone+=1
    elif seq[i] == 3:
        wrongs+=1
        threesinone+=1

for i in range(twos):
    if seq[ones+i] == 1:
        wrongs+=1
        onesintwo+=1
    elif seq[ones+i] == 3:
        wrongs+=1
        threesintwo+=1

for i in range(threes):
    if seq[ones+twos+i] == 1:
        wrongs+=1
        onesinthree+=1
    elif seq[ones+twos+i] == 2:
        twosinthree+=1


swaps += (min(onesintwo, twosinone) + min(onesinthree, threesinone) + min(twosinthree, threesintwo))
swaps += (2*(max(onesintwo, twosinone)-min(onesintwo, twosinone)))

fout.write(str(swaps) + '\n')
fout.close()