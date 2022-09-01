"""
ID: anudeep6
LANG: PYTHON3
TASK: holstein
"""

fin = open('holstein.in', 'r')
fout = open('holstein.out', 'w')
v = int(fin.readline().strip())
line = fin.readline().strip().split()
vitlevels = []
for i in range(v):
    vitlevels.append(int(line[i]))
f = int(fin.readline().strip())
feeds = [[0 for i in range(v)] for j in range(f)]
for i in range(f):
    line = fin.readline().strip().split()
    for j in range(v):
        feeds[i][j] = int(line[j])


def add(listone, listtwo):
    return [listone[counter] + listtwo[counter] for counter in range(len(listone))]

def greater(listone, listtwo):
    for count in range(len(listone)):
        if listone[count] < listtwo[count]:
            return False
    return True

minlength = 100
minset = []
count = 0
'''
def recur(feedsset):
    global count
    count += 1
    print(count, feedsset)
    global minlength
    global minset
    for i in range(1, f + 1):
        if i not in feedsset:
            feedsset.append(i)
            added = [0]*v
            for feed in feedsset:
                added = add(added, feeds[feed-1])
            if greater(added, vitlevels) and len(feedsset) < minlength:
                minset = [x for x in feedsset]
                minlength = len(feedsset)
            feedsset.remove(i)
    for i in range(1, f+1):
        if i not in feedsset:
            feedsset.append(i)
            recur(feedsset)
            feedsset.remove(i)
'''
'''
queue = []
def recur(feedset):
    for feed in feedset:
        added = add(added, feeds[feed - 1])
    if greater(added, vitlevels):
        fout.write(str(len(feedset)) + ' ' + ' '.join([str(feednum) for feednum in sorted(feedset)]) + '\n')
        exit()
    for i in range(feedset[len(feedset)-1]+1, f):
        feedset.append(i)
        queue.append(feedset)
        feedset.remove(i)

start = []
for i in range(f):
    start.append(i)
    queue.append(start)
    start.remove(i)
while len(queue) > 0:
    start = queue[0]
    recur(start)
'''

nums = [i+1 for i in range(f)]
sets = []
for i in range(1 << f):
    sets.append([nums[j] for j in range(f) if (i & (1 << j))])
sets.remove([])
for set in sets:
    added = [0]*v
    for num in set:
        added = add(added, feeds[num-1])
    if greater(added, vitlevels) and (len(set) < minlength or (len(set) == minlength and set[len(set)-1] < minset[len(minset)-1])):
        minset = [x for x in set]
        minlength = len(set)

fout.write(str(len(minset)) + ' ' + ' '.join([str(feednum) for feednum in sorted(minset)]) + '\n')
fout.close()