"""
ID: anudeep6
LANG: PYTHON2
TASK: ariprog
"""

fin = open('ariprog.in', 'r')
fout = open('ariprog.out', 'w')
n = int(fin.readline().strip())
m = int(fin.readline().strip())

max = 2*(m*m)
bisquarevals=[0]*(max+1)
bisquares = {}
for i in range(m+1):
    for j in range(i, m+1):
        add = (i*i + j*j)
        bisquarevals[add] = 1
        bisquares[add] = 1

bisquares = sorted(bisquares)
length = len(bisquares)

starts = []
'''
def check(a,b,num):
    diff = b - a
    for i in range(2, num):
        if (a + diff*i) not in bisquares:
            return False
    return True

valids = []
for i in range(length):
    for j in range(i+1, length):
        if check(bisquares[i], bisquares[j], n):
            valids.append((bisquares[i],(bisquares[j]-bisquares[i])))




valids = sorted(valids, key=lambda element: (element[1], element[0]))

if len(valids) == 0:
    fout.write('NONE\n')
else:
    for valid in valids:
        fout.write(str(valid[0]) + ' ' + str(valid[1]) + '\n')
'''

'''
def check(arr):
    if len(arr) <= 2:
        return True
    else:
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if (arr[i] - arr[i-1]) != diff:
                return False
    return True


def fill(arr, ind):
    if len(arr) == n:
        fout.write(str(arr[0]) + ' ' + str(arr[1] - arr[0]) + '\n')
        return
    else:
        for i in range(ind+1, length):
            arr.append(bisquares[i])
            if check(arr):
                print(arr, i, ind)
                fill(arr, i)
                break
            del arr[len(arr)-1]

fill([], -1)
'''

min = 0
#max = 2*(m*m)
valids = []
print(bisquares[length-30:length-1])

def check(a,b,n):
    for i in range(n):
        if not bisquarevals[a+i*b]:
            return False
    return True
'''
def check(a,b,n):
    for i in range(n):
        if not bisquarevals[a-i*b]:
            return False
    return True
'''

for i in range(length-1, n-2, -1):
    a = bisquares[i]
    #b=1
    #while (a+(n-1)*b) <= max:
    #for b in range(bisquares[i+1]-a, int((max-a)/(n-1)) + 1):
    for j in range(i-1, -1, -1):
        b = a - bisquares[j]
        if b > (a/(n-1)):
            break
        if check(a-(n-1)*b,b,n):
            print(i, a, b)
            valids.append((a-(n-1)*b,b))
        #b+=1


'''
for i in range(int(length)):
    a = bisquares[i]
    #b=1
    #while (a+(n-1)*b) <= max:
    #for b in range(bisquares[i+1]-a, int((max-a)/(n-1)) + 1):
    for j in range(i+1, length):
        b = bisquares[j] - a
        if b > int((max-a)/(n-1)):
            break
        if check(a,b,n):
            print(i, a, b)
            valids.append((a,b))
        #b+=1
'''
'''
for i in range(max):
    if not bisquarevals[i]:
        continue
    for j in range(1, int((max-i) / (n - 1) + 1)):
        print(i,j)
        for k in range(n):
            if not bisquarevals[i + j * k]:
                break
            valids.append((i, j))
'''
valids = sorted(valids, key=lambda element: (element[1], element[0]))

if len(valids) == 0:
    fout.write('NONE\n')
else:
    for valid in valids:
        fout.write(str(valid[0]) + ' ' + str(valid[1]) + '\n')

fout.close()