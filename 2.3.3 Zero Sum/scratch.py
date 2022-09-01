"""
ID: anudeep6
LANG: PYTHON3
TASK: zerosum
"""


fin = open('zerosum.in', 'r')
fout = open('zerosum.out', 'w')

n = int(fin.readline().strip())
#[+, -,  ]
oks = []

def ok(list):
    sum = 1
    i = 0
    while i < (n - 1):
        if list[i] == 1:
            sum += (i + 2)
            i+=1
        elif list[i] == 2:
            sum -= (i + 2)
            i+=1
        else:
            temp = i+1
            while temp < n-1 and list[temp] == 0:
                temp+=1
            if i == 0 or list[i-1] == 1:
                sum -= (i + 1)
                for x in range(temp-i+1):
                    sum += (i + 1 + x)*10**(temp-i-x)
                i = temp
            else:
                sum += (i + 1)
                for x in range(temp - i+1):
                    sum -= (i + 1 + x) * 10 ** (temp - i - x)
                i = temp
    return sum == 0

def recur(arr):
    global oks
    global count
    if len(arr) == n-1:
        if ok(arr):
            oks.append(arr.copy())
        return
    else:
        for i in range(3):
            arr.append(i)
            recur(arr)
            del(arr[-1])

recur([])

print(oks)



'''
  sum = 0
        prev = 0
        if arr[0] == 0:
            sum += (1+2)
        elif arr[0] == 1:
            sum += (1-2)
        else:
            sum += (12)
            prev = 12
        for i in range(n-1):
            if arr[i] == 0:
                sum += (i+2)
            elif arr[i] == 1:
                sum -= (i+2)
            else:
                if arr[i-1] == 0:
                    sum -= (i + 1)
                    sum += (10*(i+1) + i+2)
                    prev = (10*(i+1) + i+2)
                elif arr[i-1] == 1:
                    sum += (i + 1)
                    sum -= (10 * (i + 1) + i + 2)
                    prev = (10 * (i + 1) + i + 2)
                else:
                    sum += ()
'''
opers = {1: '+', 2: '-', 0: ' '}
expression = ['']*(2*n-1)
for i in range(n):
    expression[2*i] = str(i+1)
for ops in oks:
    for i in range(n-1):
        expression[2 * i + 1] = opers[ops[i]]
    fout.write(''.join(expression) + '\n')

fout.close()