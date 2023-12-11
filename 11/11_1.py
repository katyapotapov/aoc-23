import re
import math
import copy

with open("input.txt") as f:
    ls = f.readlines()

rows_ls = []
inc_val = 2
for i in range(len(ls)):
    if set(ls[i]) == set([".", "\n"]):
        for _ in range(inc_val):
            rows_ls.append(list(ls[i].strip()))
    else:
        rows_ls.append(list(ls[i].strip()))

new_ls = []
import numpy as np
rows_ls_np = np.array(rows_ls).T.tolist()
print(rows_ls_np)
for i in range(len(rows_ls_np)):
    if set(rows_ls_np[i]) == set(["."]):
        for _ in range(inc_val):
            new_ls.append(list(rows_ls_np[i]))
    else:
        new_ls.append(list(rows_ls_np[i]))


print(len(rows_ls_np))
print(len(new_ls))

cur_galaxy_num = 0
galaxy_pos = []
for i in range(len(new_ls)):
    for j in range(len(new_ls[0])):
        if new_ls[i][j] == "#":
            new_ls[i][j] = cur_galaxy_num
            galaxy_pos.append((i, j))
            cur_galaxy_num += 1

print(new_ls)

all_galaxy_paths = {}

for i in range(len(galaxy_pos)):
    for j in range(i, len(galaxy_pos)):
        all_galaxy_paths[(i, j)] = abs(galaxy_pos[i][0] - galaxy_pos[j][0]) + abs(galaxy_pos[i][1] -
                galaxy_pos[j][1])

print(sum(all_galaxy_paths.values()))
