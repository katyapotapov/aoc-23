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

ls_vals = [[-1] * len(ls[0]) for l in ls]

ls_vals[s_pos[0]][s_pos[1]] = 0

maybe_loops = []


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


# print(max_val)
# print(math.ceil(max_val/2))

print("checking loop")

import sys
sys.setrecursionlimit(1000000)

def check_loop(ls_vals, cur_loop):
    print(f"{cur_loop[-1][0]}, {cur_loop[-1][1]}")
    cur_val = ls_vals[cur_loop[-1][0]][cur_loop[-1][1]]
    if cur_loop[-1][0] > 0:
        val = ls_vals[cur_loop[-1][0]-1][cur_loop[-1][1]]
        cur_coord = [(cur_loop[-1][0]-1, cur_loop[-1][1])]
        if val == cur_val + 1:
            loop = check_loop(ls_vals, cur_loop + cur_coord)
            if len(loop) > 0:
                return loop 
        if val == 0 and cur_val == max_val:
            return cur_loop + cur_coord
            
    if cur_loop[-1][0] < len(ls_vals)-1:
        val = ls_vals[cur_loop[-1][0]+1][cur_loop[-1][1]] 
        cur_coord = [(cur_loop[-1][0]+1, cur_loop[-1][1])]
        if val == cur_val + 1:
            loop = check_loop(ls_vals, cur_loop + cur_coord)
            if len(loop) > 0:
                return loop
        if val == 0 and cur_val == max_val:
            return cur_loop + cur_coord

    if cur_loop[-1][1] < len(ls_vals[0])-1:
        val = ls_vals[cur_loop[-1][0]][cur_loop[-1][1]+1] 
        cur_coord = [(cur_loop[-1][0], cur_loop[-1][1]+1)]
        if val == cur_val + 1:

            loop = check_loop(ls_vals, cur_loop + cur_coord)
            if len(loop) > 0:
                return loop
        if val == 0 and cur_val == max_val:
            return cur_loop + cur_coord

    if cur_loop[-1][1] > 0:
        val = ls_vals[cur_loop[-1][0]][cur_loop[-1][1]-1]
        cur_coord = [(cur_loop[-1][0], cur_loop[-1][1]-1)]
        if val == cur_val + 1:
            loop = check_loop(ls_vals, cur_loop + cur_coord)
            if len(loop) > 0:
                return loop
        if val == 0 and cur_val == max_val:
            return cur_loop + cur_coord
    return []
    print(cur_val)

print("loop")
loop = check_loop(ls_vals, [s_pos])

enclosed_tiles = 0
for i in range(len(ls_vals)):
    for j in range(len(ls_vals[0])):
        if ls_vals[i][j] == -1:

            def get_num_loop_int(i, j):
                j_val = j
                num_loop_int = 0
                to_check_val = None

                while j_val >= 0:
                    if (i, j_val) in loop and ls[i][j_val] in "|":
                        num_loop_int += 1
                    if (i, j_val) in loop and ls[i][j_val] in "L7FJ":
                        if to_check_val is not None:
                            pair = set([to_check_val, ls[i][j_val]])
                            if pair == set(list("L7")) or pair == set(list("FJ")):
                                num_loop_int += 1
                            to_check_val = None
                        else:
                            to_check_val = ls[i][j_val]
                    print(j_val)
                    j_val -= 1
                if j_val == -1:
                    return num_loop_int

                # j_val = j
                # while j_val < len(ls[0]):
                #     if ls[i][j_val] in "L7FJ":
                #         break
                #     if (i, j_val) in loop and ls[i][j_val] in "|":
                #         num_loop_int += 1
                #     j_val += 1

                # if j_val == len(ls[0]):
                #     return num_loop_int

                # i_val = i
                # while i_val < len(ls):
                #     print(f"{i_val=}")
                #     print(f"{len(ls[0])=}")
                #     if ls[i_val][j] in "L7FJ":
                #         break
                #     if (i_val, j) in loop and ls[i_val][j] in "-":
                #         num_loop_int += 1
                #     i_val += 1

                # if i_val == len(ls):
                #     return num_loop_int

                # i_val = i
                # while i_val > 0:
                #     if ls[i_val][j] in "L7FJ":
                #         break
                #     if (i_val, j) in loop and ls[i_val][j] in "-":
                #         num_loop_int += 1
                #     i_val -= 1

                # if i_val == 0:
                #     return num_loop_int

            num_loop_int = get_num_loop_int(i, j)

            if num_loop_int is None:
                print(f"Ahh omg this coord is messed up {(i, j)}")
                continue
            if num_loop_int % 2 == 1:
                print((i, j))
                print(num_loop_int)
                enclosed_tiles += 1 

print(enclosed_tiles)

