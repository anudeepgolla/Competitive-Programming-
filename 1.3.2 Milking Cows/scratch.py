"""
ID: anudeep6
LANG: PYTHON2
TASK: milk2
"""

fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')
n = int(fin.readline().strip())
points = {}
for i in range(n):
    line = fin.readline().strip().split()
    if int(line[0]) in points:
        points[int(line[0])] += 1
    else:
        points[int(line[0])] = 1
    if int(line[1]) in points:
        points[int(line[1])] -= 1
    else:
        points[int(line[1])] = -1


maxontime = 0
maxdowntime = 0
curontime = 0
curdowntime = 0
sortedpts = sorted(points)
prev = sortedpts[0]
farmers = 1
for i in range(1, len(sortedpts)):
    if farmers > 0:
        curdowntime = 0
        curontime += (sortedpts[i] - prev)
        farmers += points[sortedpts[i]]
    else:
        curontime = 0
        curdowntime += (sortedpts[i] - prev)
        farmers += points[sortedpts[i]]
    if curdowntime > maxdowntime:
        maxdowntime = curdowntime
    if curontime > maxontime:
        maxontime = curontime
    prev = sortedpts[i]
    #print(sortedpts[i], maxontime, maxdowntime, curontime, curdowntime, farmers)


fout.write(str(maxontime) + ' ' + str(maxdowntime) + '\n')
fout.close()

'''
fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')
n = int(fin.readline().strip())
start = 1000000
end = 0
firsts = []
seconds = []
for i in range(n):
    line = fin.readline().strip().split()
    first = int(line[0])
    second = int(line[1])
    if first < start:
        start = first
    if second > end:
        end = second
    firsts.append(first)
    seconds.append(second)
idle = False
maxontime = 0
maxdowntime = 0
curontime = 0
curdowntime = 0
for i in range(start, end):
    j = 0
    while j < n and (i < firsts[j] or i >= seconds[j]):
        j += 1
    if j != n and idle == False:
        curontime += 1
    elif j != n and idle == True:
        idle = False
        if curdowntime > maxdowntime:
            maxdowntime = curdowntime
        curdowntime = 0
        curontime = 1
    elif j == n and idle == False:
        idle = True
        if curontime > maxontime:
            maxontime = curontime
        curontime = 0
        curdowntime = 1
    else:
        curdowntime += 1
    #print(i, curontime, curdowntime, maxontime, maxdowntime)
if curdowntime > maxdowntime:
    maxdowntime = curdowntime
if curontime > maxontime:
    maxontime = curontime

fout.write(str(maxontime) + ' ' + str(maxdowntime) + '\n')
fout.close()
'''