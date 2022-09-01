"""
ID: anudeep6
LANG: PYTHON2
TASK: transform
"""
import numpy as np

fin = open('transform.in', 'r')
fout = open('transform.out', 'w')
n = int(fin.readline().strip())
#rows = {}
#columns = {}
origarray = np.array([['' for i in range(n)] for j in range(n)])
for i in range(n):
    line = fin.readline().strip()
    array = []
    for j in range(n):
        array.append(line[j])
    origarray[i] = array

transform = origarray.copy()
for i in range(n):
    line = fin.readline().strip()
    array = []
    for j in range(n):
        array.append(line[j])
    transform[i] = array

array1 = origarray.copy()
for i in range(n):
    array1[i] = list(reversed(origarray[:, i]))

array2 = origarray.copy()
for i in range(n):
    array2[i] = list(reversed(origarray[n-1-i]))

array3 = origarray.copy()
for i in range(n):
    array3[i] = origarray[:, n-1-i]

array4 = origarray.copy()
for i in range(n):
    array4[i] = list(reversed(origarray[i]))

array5 = origarray.copy()
for i in range(n):
    array5[i] = list(reversed(array4[:, i]))

array6 = origarray.copy()
for i in range(n):
    array6[i] = list(reversed(array4[n-1-i]))

array7 = origarray.copy()
for i in range(n):
    array7[i] = array4[:, n-1-i]

result = 0
if (transform == array1).all():
    result = 1
elif (transform == array2).all():
    result = 2
elif (transform == array3).all():
    result = 3
elif (transform == array4).all():
    result = 4
elif (transform == array5).all():
    result = 5
elif (transform == array6).all():
    result = 5
elif (transform == array7).all():
    result = 5
elif (transform == origarray).all():
    result = 6
else:
    result = 7


fout.write(str(result) + '\n')
fout.close()