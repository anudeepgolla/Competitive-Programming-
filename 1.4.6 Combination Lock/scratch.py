"""
ID: anudeep6
LANG: PYTHON2
TASK: combo
"""
import numpy as np

fin = open('combo.in', 'r')
fout = open('combo.out', 'w')
n = int(fin.readline().strip())
farmer = fin.readline().strip().split()
master = fin.readline().strip().split()

def convert(x,range):
    if x <= 0:
        return (x + range)
    elif x > range:
        return (x - range)
    else:
        return x
remove = []
poss = {}

if n < 6:
    result = np.power(n,3)
else:
    for i in range(3):
        farm = int(farmer[i])
        mast = int(master[i])

        poss[convert(farm-2, n)] = 1
        poss[convert(farm - 1, n)] = 1
        poss[convert(farm - 0, n)] = 1
        poss[convert(farm + 1, n)] = 1
        poss[convert(farm + 2, n)] = 1
        poss[convert(mast - 2, n)] = 1
        poss[convert(mast - 1, n)] = 1
        poss[convert(mast - 0, n)] = 1
        poss[convert(mast + 1, n)] = 1
        poss[convert(mast + 2, n)] = 1

        #print(poss)
        remove.append(len(poss))
        poss={}
    #print(remove)
    prod = 1
    for i in range(3):
        prod *= (10-remove[i])
    result = 250 - prod

fout.write(str(result) + '\n')
fout.close()