"""
ID: anudeep6
LANG: PYTHON3
TASK: runround
"""

fin = open('runround.in', 'r')
fout = open('runround.out', 'w')
n = int(fin.readline().strip())
ncopy = n
length = 0
while(ncopy):
    length+=1
    ncopy = int(ncopy/10)

digits = [0,1,2,3,4,5,6,7,8,9]
curdig=[]



def recur(num, digleft):
    if num == length:
        nums.append(curdig.copy())
        #print(nums)
        return
    else:
        for dig in digleft:
            curdig.append(dig)
            temp = digleft.copy()
            temp.remove(dig)
            recur(num+1, temp)
            curdig.remove(dig)

def run(digs):
    visited=set()
    iter = 0
    count = 0
    while count < len(digs):
        numtoadd = digs[(iter+digs[iter])%len(digs)]
        if numtoadd in visited:
            return False
        visited.add(numtoadd)
        iter = (iter + digs[iter]) % len(digs)
        count+=1
    if iter == 0:
        return True
    return False


while length<10:
    nums = []
    recur(0, {1,2,3,4,5,6,7,8,9})
    for num in nums:
        if run(num) and sum((10**x)*(num[len(num)-1-x]) for x in range(len(num))) > n:
            fout.write(str(sum((10**x)*(num[len(num)-1-x]) for x in range(len(num))))+ '\n')
            fout.close()
            exit()
    length+=1

