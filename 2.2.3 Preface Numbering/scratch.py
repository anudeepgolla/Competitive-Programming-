"""
ID: anudeep6
LANG: PYTHON3
TASK: preface
"""

fin = open('preface.in', 'r')
fout = open('preface.out', 'w')
n = int(fin.readline().strip())

first = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] #1-10
second = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] #10-90
third = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] #100-900
fourth = ["M", "MM", "MMM"] #1000-3000

numerals = ['0']*3500
for i in range(9):
    numerals[i] = first[i]
for i in range(1,10):
    numerals[10*i-1] = second[i-1]

for i in range(9):
    for j in range(10*(i+1), 10*(i+1)+9):
        numerals[j] = numerals[10*(i+1)-1] + numerals[j%10]

for i in range(1,10):
    numerals[100 * i - 1] = third[i-1]

for i in range(9):
    for j in range(100*(i+1), 100*(i+1)+99):
        numerals[j] = numerals[100*(i+1)-1] + numerals[j%100]

for i in range(1,4):
    numerals[1000 * i - 1] = fourth[i - 1]

for i in range(3):
    for j in range(1000*(i+1), 1000*(i+1)+999):
        numerals[j] = numerals[1000 * (i + 1) - 1] + numerals[j % 1000]
        if j == 3499:
            break

vals = {'I':0, 'V':0, 'X':0, 'L':0, 'C':0, 'D':0, 'M':0}
for i in range(n):
    for j in range(len(numerals[i])):
        vals[numerals[i][j]] += 1


for letter in vals:
    if vals[letter]!=0:
        fout.write(letter + ' ' + str(vals[letter]) + '\n')
fout.close()