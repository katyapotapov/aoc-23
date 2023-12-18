import re

with open("input_long.txt") as f:
    ls = f.readlines()

insts = []
for l in ls:
    insts.append((int("0x" + l[l.find("#")+1:l.find(")")-1], 16), int(l[l.find(")")-1])))

insts[0] = (insts[0][0]+1, insts[0][1])

init_pt = (0, 0)
pts = [(0, 0)]
for i, (l, d) in enumerate(insts):
    if d == 0:
        pts.append((pts[-1][0], pts[-1][1]+l))
    elif d == 2:
        pts.append((pts[-1][0], pts[-1][1]-l))
    elif d == 1:
        pts.append((pts[-1][0]+l, pts[-1][1]))
    elif d == 3:
        pts.append((pts[-1][0]-l, pts[-1][1]))




lowest_i = min(pts, key=lambda pt: pt[0])[0]
lowest_j = min(pts, key=lambda pt: pt[1])[1]

pts = [(i - lowest_i, j) for i, j in pts]
pts = [(i, j - lowest_j) for i, j in pts]


# ok i got this from https://stackoverflow.com/questions/451426/how-do-i-calculate-the-area-of-a-2d-polygon
# segments = zip(pts, pts[1:] + [pts[0]])
# 
# area = (abs(sum(i0*j1 - j1*y0`

print(pts)

area = 0
for x in range(len(pts)):
    y = (x+1)%len(pts)
    area += pts[x][0] * pts[y][1]
    area -= pts[x][1] * pts[y][0]



print(area/2)

p = sum([inst[0] for inst in insts])

print(p)

print((abs(area)+abs(p))/2)
