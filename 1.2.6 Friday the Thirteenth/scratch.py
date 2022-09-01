"""
ID: anudeep6
LANG: PYTHON2
TASK: friday
"""
fin = open('friday.in', 'r')
fout = open('friday.out', 'w')
n = int(fin.readline().strip())
days = [0,0,0,0,0,0,0]
curday = 2
for i in range(1900, 1900+n):
    leap = (i % 4 == 0)
    if i % 100 == 0 and i % 400 != 0:
        leap = False
    curday = (curday + 12) % 7
    days[curday] += 1
    curday = (curday + 31) % 7
    days[curday] += 1
    if leap:
        curday = (curday + 29) % 7
        days[curday] += 1
    else:
        curday = (curday + 28) % 7
        days[curday] += 1
    curday = (curday + 31) % 7
    days[curday] += 1
    curday = (curday + 30) % 7
    days[curday] += 1
    curday = (curday + 31) % 7
    days[curday] += 1
    curday = (curday + 30) % 7
    days[curday] += 1
    curday = (curday + 31) % 7
    days[curday] += 1
    curday = (curday + 31) % 7
    days[curday] += 1
    curday = (curday + 30) % 7
    days[curday] += 1
    curday = (curday + 31) % 7
    days[curday] += 1
    curday = (curday + 30) % 7
    days[curday] += 1
    curday = (curday + 19) % 7


fout.write(str(int(days[0])) + ' ' + str(int(days[1])) + ' ' + str(int(days[2])) + ' ' + str(int(days[3])) + ' ' + str(int(days[4])) + ' ' +
           str(int(days[5])) + ' ' + str(int(days[6])) + '\n')
fout.close()

# 31 28 31 30 31 30 31 31 30 31 30 31