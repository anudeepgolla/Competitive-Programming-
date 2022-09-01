"""
ID: anudeep6
LANG: PYTHON2
TASK: crypt1
"""
import numpy as np

fin = open('crypt1.in', 'r')
fout = open('crypt1.out', 'w')
n = int(fin.readline().strip())
nums = fin.readline().strip().split()



def accept(x, set):
    while(x):
        rem = (x % 10)
        if str(rem) not in set:
            return False
        x = int(x/10)
    return True

count = 0
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                for e in range(n):
                    first = (100*int(nums[a]) + 10*int(nums[b]) + int(nums[c])) * int(nums[d])
                    second = (100*int(nums[a]) + 10*int(nums[b]) + int(nums[c])) * int(nums[e])
                    result = 10*first+second
                    if first < 1000 and second < 1000 and result < 10000 and accept(first, nums) \
                            and accept(second, nums) and accept(result, nums):
                        count += 1



fout.write(str(count) + '\n')
fout.close()