import re
import math
import copy

with open("input.txt") as f:
    ls = f.readlines()

for i in range(len(ls)):
    if "S" in ls[i]:
        s_pos = (i, ls[i].find("S"))
        print(s_pos)
    ls[i] = list(ls[i].strip())

frontier = [s_pos]
seen_before = []

ls_vals = [[0] * len(ls[0]) for l in ls]

ls_vals[s_pos[0]][s_pos[1]] = 0


while len(frontier) > 0:
    cur_pos = frontier.pop()
    # if cur_pos in seen_before:
    #     continue
    seen_before.append(cur_pos)

    cur_val = ls_vals[cur_pos[0]][cur_pos[1]]
    cur_pipe = ls[cur_pos[0]][cur_pos[1]]
    if cur_pipe in "|LJS" and cur_pos[0] > 0:
        if (cur_pos[0]-1, cur_pos[1]) not in seen_before and ls[cur_pos[0]-1][cur_pos[1]] in "|F7":
            ls_vals[cur_pos[0]-1][cur_pos[1]] = cur_val + 1
            frontier.append((cur_pos[0]-1, cur_pos[1]))
    if cur_pipe in "|F7S" and cur_pos[0] < len(ls)-1:
        if (cur_pos[0]+1, cur_pos[1]) not in seen_before and ls[cur_pos[0]+1][cur_pos[1]] in "|LJ":
            print(f"{cur_pos=}")
            print(cur_val)
            ls_vals[cur_pos[0]+1][cur_pos[1]] = cur_val + 1
            frontier.append((cur_pos[0]+1, cur_pos[1]))

    # left right
    if cur_pipe in "-LFS" and cur_pos[1] < len(ls[0])-1:
        if (cur_pos[0], cur_pos[1]+1) not in seen_before and ls[cur_pos[0]][cur_pos[1]+1] in "-J7":
            ls_vals[cur_pos[0]][cur_pos[1]+1] = cur_val + 1
            frontier.append((cur_pos[0], cur_pos[1]+1))
    if cur_pipe in "-7JS" and cur_pos[1] > 0:
        if (cur_pos[0], cur_pos[1]-1) not in seen_before and ls[cur_pos[0]][cur_pos[1]-1] in "-LF":
            ls_vals[cur_pos[0]][cur_pos[1]-1] = cur_val + 1
            frontier.append((cur_pos[0], cur_pos[1]-1))


[print(i) for i in ls_vals]

max_val = 0
for l in ls_vals:
    for i in l:
        max_val = max(max_val, i)


print(max_val)
print(math.ceil(max_val/2))
