"""
ID: anudeep6
LANG: PYTHON3
TASK: lamps
"""


#[1,1,1,1,1,1]
#[0,0,0,0,0,0] 1
#[0,1,0,1,0,1] 2
#[1,0,1,0,1,0] 3
#[0,1,1,0,1,1] 4
#[1,0,1,0,1,0] 1,2
#[0,1,0,1,0,1] 1,3
#[1,0,0,1,0,0] 1,4
#[0,0,0,0,0,0] 2,3
#[1,1,0,0,0,1] 2,4
#[0,0,1,1,1,0] 3,4
#[1,1,1,1,1,1] 1,2,3
#[0,0,1,1,1,0] 1,2,4
#[1,1,0,0,0,1] 1,3,4
#[1,0,0,1,0,0] 2,3,4
#[0,1,1,0,1,1] 1,2,3,4

#[1,1,1,1,1,1]
#[0,0,0,0,0,0]
#[0,1,0,1,0,1]
#[1,0,1,0,1,0]
#[0,1,1,0,1,1]
#[1,0,0,1,0,0]
#[1,1,0,0,0,1]
#[0,0,1,1,1,0]


fin = open('lamps.in', 'r')
fout = open('lamps.out', 'w')
n = int(fin.readline().strip())
c = int(fin.readline().strip())
line = fin.readline().strip().split()
ons = []
for i in range(len(line)-1):
    ons.append(int(line[i]))
line = fin.readline().strip().split()
offs = []
for i in range(len(line)-1):
    offs.append(int(line[i]))

if c == 1:
    poss = [[0,0,0,0,0,0],
            [0,1,0,1,0,1],
            [0,1,1,0,1,1],
            [1,0,1,0,1,0]]
else:
    poss = [[0,0,0,0,0,0],
            [0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 1, 1],
            [1, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1]]


if c == 0:
    if len(ons) == 0 and len(offs) == 0:
        ans = []
        for i in range(n):
            ans.append('1')
        fout.write(''.join(ans) + '\n')
        fout.close()
        exit()
    else:
        fout.write('IMPOSSIBLE\n')
        fout.close()
        exit()


succ = []
for pos in poss:
    cont = True
    for on in ons:
        if pos[on%6 - 1] != 1:
            cont = False
            break
    if cont:
        for off in offs:
            if pos[off % 6 - 1] != 0:
                cont = False
                break
    if cont:
        succ.append(pos)


answers = []


if len(succ) == 0:
    fout.write('IMPOSSIBLE\n')
    fout.close()
    exit()

for suc in succ:
    ans = []
    for i in range(n):
        ans.append(str(suc[i%6]))
    answers.append(ans)

for answ in answers:
    fout.write(''.join(answ) + '\n')
fout.close()


