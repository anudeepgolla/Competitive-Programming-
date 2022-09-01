"""
ID: anudeep6
LANG: PYTHON2
TASK: castle
"""
import numpy as np

fin = open('castle.in', 'r')
fout = open('castle.out', 'w')
line = fin.readline().strip().split()
width = int(line[0])
height = int(line[1])

rooms = {}
numcomponents = 0
squares = [0]*(height*width)

for x in range(height):
    line = fin.readline().strip().split()
    for y in range(width):
        squares[x*width + y] = int(line[y])

'''
setone = {0,2,4,8,6,10,12,14}
settwo = {0, 1, 4, 8, 5, 9, 12, 13}
setthree = {0, 1, 2, 8, 3, 9, 10, 11}
setfour = {0, 1, 2, 4, 3, 5, 6, 7}

def neighbor(i, h, w):
    total = h*w
    neighbors = [i - w, i + w, i + 1, i - 1]
    if i == 0:
        if i-w in neighbors:
            neighbors.remove(i-w)
        if i-1 in neighbors:
            neighbors.remove(i-1)
    if i == w - 1:
        if i-w in neighbors:
            neighbors.remove(i-w)
        if i+1 in neighbors:
            neighbors.remove(i+1)
    if i == (total - w):
        if i+w in neighbors:
            neighbors.remove(i+w)
        if i-1 in neighbors:
            neighbors.remove(i-1)
    if i == (total - 1):
        if i+w in neighbors:
            neighbors.remove(i+w)
        if i+1 in neighbors:
            neighbors.remove(i+1)
    if 0 < i < w - 1:
        if i-w in neighbors:
            neighbors.remove(i-w)
    if total - w < i < total - 1:
        if i+w in neighbors:
            neighbors.remove(i+w)
    if i % w == w - 1:
        if i+1 in neighbors:
            neighbors.remove(i+1)
    if i % w == 0:
        if i-1 in neighbors:
            neighbors.remove(i-1)
    
    if i == 0:
        neighbors = [i + w, i + 1]
    elif i == w-1:
        neighbors = [i + w, i - 1]
    elif i == (total - w):
        neighbors = [i - w, i + 1]
    elif i == (total-1):
        neighbors = [i - w, i - 1]
    elif 0 < i < w-1:
        neighbors = [i + w, i + 1, i - 1]
    elif total - w < i < total - 1:
        neighbors = [i - w, i + 1, i - 1]
    elif i % w == w-1:
        neighbors = [i - w, i + w, i - 1]
    elif i % w == 0:
        neighbors = [i - w, i + w, i + 1]
    else:
        neighbors = [i - w, i + w, i + 1, i - 1]
    

    if squares[i] not in setone:
        if i-1 in neighbors:
            neighbors.remove(i-1)
    if squares[i] not in settwo:
        if i-w in neighbors:
            neighbors.remove(i-w)
    if squares[i] not in setthree:
        if i+1 in neighbors:
            neighbors.remove(i+1)
    if squares[i] not in setfour:
        if i+w in neighbors:
            neighbors.remove(i+w)

    return neighbors
'''
def nbnorest(i, h, w):
    total = h * w
    neighbors = [i - w, i + w, i + 1, i - 1]
    if i == 0:
        if i - w in neighbors:
            neighbors.remove(i - w)
        if i - 1 in neighbors:
            neighbors.remove(i - 1)
    if i == w - 1:
        if i - w in neighbors:
            neighbors.remove(i - w)
        if i + 1 in neighbors:
            neighbors.remove(i + 1)
    if i == (total - w):
        if i + w in neighbors:
            neighbors.remove(i + w)
        if i - 1 in neighbors:
            neighbors.remove(i - 1)
    if i == (total - 1):
        if i + w in neighbors:
            neighbors.remove(i + w)
        if i + 1 in neighbors:
            neighbors.remove(i + 1)
    if 0 < i < w - 1:
        if i - w in neighbors:
            neighbors.remove(i - w)
    if total - w < i < total - 1:
        if i + w in neighbors:
            neighbors.remove(i + w)
    if i % w == w - 1:
        if i + 1 in neighbors:
            neighbors.remove(i + 1)
    if i % w == 0:
        if i - 1 in neighbors:
            neighbors.remove(i - 1)
    return neighbors


def newneighbors(s, hi, wi):
    state = squares[s]
    binary = int(bin(state)[2:])
    result = [s - wi, s + wi, s + 1, s - 1]
    temp = [s + wi, s + 1, s - wi, s - 1]
    count = 3
    while binary:
        if binary % 10:
            #print(binary, result, count)
            result.remove(temp[count])
        count -= 1
        binary = int(binary/10)
    return result

toadd = set()

def flood_fill(numcomp):
    '''
    notdone = True
    while(notdone):
        numvisited = 0
        for square in range(height*width):
            if square in rooms and rooms[square] == -2:
                numvisited += 1
                rooms[square] = numcomp
                #print(square, neighbor(square, height, width))
                for nb in newneighbors(square, height, width):
                    if nb not in rooms:
                        rooms[nb] = -2
                        numvisited += 1
        if numvisited == 0:
            notdone = False
    '''
    while len(toadd) != 0:
        for square in toadd:
                rooms[square] = numcomp
                toadd.remove(square)
                # print(square, neighbor(square, height, width))
                for nb in newneighbors(square, height, width):
                    if nb not in rooms:
                        toadd.add(nb)
                break

for i in range(height*width):
    if i not in rooms:
        numcomponents += 1
        #rooms[i] = -2
        toadd.add(i)
        flood_fill(numcomponents)

roomsizes = {}
for key in rooms:
    if rooms[key] not in roomsizes:
        roomsizes[rooms[key]] = 1
    else:
        roomsizes[rooms[key]] += 1

length = len(roomsizes)
sizes = []
for key in roomsizes:
    sizes.append(roomsizes[key])
sizes = sorted(sizes)
maxroom = sizes[len(sizes) - 1]
maxposscomb = sizes[len(sizes) - 1] + sizes[len(sizes) - 2]
maxcomb = 0
wall = (0, width, 'E')


for square in range(height*width):
    for nb in nbnorest(square, height, width):
        if rooms[square] != rooms[nb]:
            if roomsizes[rooms[square]] + roomsizes[rooms[nb]] > maxcomb:
                print(maxcomb, wall)
                maxcomb = roomsizes[rooms[square]] + roomsizes[rooms[nb]]
                if square - nb == width:
                    wall = (int(square/width) + 1, (square % width) + 1, 'N')
                elif nb - square == width:
                    wall = (int(nb / width) + 1, (nb % width) + 1, 'N')
                elif square - nb == 1:
                    wall = (int(nb / width) + 1, (nb % width) + 1, 'E')
                elif nb - square == 1:
                    wall = (int(square / width) + 1, (square % width) + 1, 'E')
                #if maxcomb == maxposscomb:
                    #break
            elif roomsizes[rooms[square]] + roomsizes[rooms[nb]] == maxcomb:
                if square - nb == width and ((square % width) + 1 < wall[1] or (
                        (square % width) + 1 == wall[1] and int(square / width) + 1 > wall[0])):
                    wall = (int(square / width) + 1, (square % width) + 1, 'N')
                elif nb - square == width and (
                        (nb % width) + 1 < wall[1] or ((nb % width) + 1 == wall[1] and int(nb / width) + 1 > wall[0])):
                    wall = (int(nb / width) + 1, (nb % width) + 1, 'N')
                elif square - nb == 1 and (
                        (nb % width) + 1 < wall[1] or ((nb % width) + 1 == wall[1] and int(nb / width) + 1 > wall[0])):
                    wall = (int(nb / width) + 1, (nb % width) + 1, 'E')
                elif nb - square == 1 and ((square % width) + 1 < wall[1] or (
                        (square % width) + 1 == wall[1] and int(square / width) + 1 > wall[0])):
                    wall = (int(square / width) + 1, (square % width) + 1, 'E')


'''

for i in range(height):
    for j in range(width-1):
        square = i*width + j
        if rooms[square] != rooms[square+1] and roomsizes[rooms[square]] + roomsizes[rooms[square + 1]] > maxcomb:
            maxcomb = roomsizes[rooms[square]] + roomsizes[rooms[square+1]]
            wall = (i+1, j+1, 'E')
        elif rooms[square] != rooms[square+1] and roomsizes[rooms[square]] + roomsizes[rooms[square + 1]] == maxcomb and (
                j+1 < wall[1] or (j+1 == wall[1] and i+1 > wall[0])):
            wall = (i + 1, j + 1, 'E')


for i in range(height-1):
    for j in range(width):
        square = i*width + j
        if rooms[square] != rooms[square+width] and roomsizes[rooms[square]] + roomsizes[rooms[square + width]] > maxcomb:
            maxcomb = roomsizes[rooms[square]] + roomsizes[rooms[square+width]]
            wall = (i+2, j+1, 'N')
        elif rooms[square] != rooms[square+width] and roomsizes[rooms[square]] + roomsizes[rooms[square + width]] == maxcomb and (
                j+1 < wall[1] or (j+1 == wall[1] and i+2 > wall[0]) or (wall == (i+2, j+1, 'E'))):
            wall = (i + 2, j + 1, 'N')
'''

fout.write(str(length) + '\n')
fout.write(str(maxroom) + '\n')
fout.write(str(maxcomb) + '\n')
fout.write(str(wall[0]) + ' ' + str(wall[1]) + ' ' + str(wall[2]) + '\n')
fout.close()