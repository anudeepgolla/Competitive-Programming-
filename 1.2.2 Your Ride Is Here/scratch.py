"""
ID: anudeep6
LANG: PYTHON2
TASK: ride
"""
fin = open('ride.in', 'r')
fout = open('ride.out', 'w')
lines = fin.readlines()
prodone = 1
prodtwo = 1
for i in range(len(lines[0])):
    prodone *= (ord(lines[0][i]) - 64)
for i in range(len(lines[1])):
    prodtwo *= (ord(lines[1][i]) - 64)
if (prodone % 47) == (prodtwo % 47):
    output = 'GO'
else:
    output = 'STAY'
fout.write(output + '\n')
fout.close()