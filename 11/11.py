import re
import math
import copy

with open("input.txt") as f:
    ls = f.readlines()

rows_ls = []
inc_val = 1

empty_i = []
empty_j = []
for i in range(len(ls)):
    if set(ls[i]) == set([".", "\n"]):
        empty_i.append(i)
    rows_ls.append(list(ls[i].strip()))

new_ls = []
import numpy as np
rows_ls_np = np.array(rows_ls).T.tolist()
for i in range(len(rows_ls_np)):
    if set(rows_ls_np[i]) == set(["."]):
        empty_j.append(i)
    new_ls.append(list(rows_ls_np[i]))

new_ls = np.array(new_ls).T.tolist()


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


all_galaxy_paths = {}

num_inc = 1000000
print(f"{galaxy_pos=}")
print(f"{empty_i=}")
print(f"{empty_j=}")
for i in range(len(galaxy_pos)):
    for j in range(i+1, len(galaxy_pos)):
        if (i, j) in all_galaxy_paths:
            raise Exception("Repeat path")
        all_galaxy_paths[(i, j)] = abs(galaxy_pos[i][0] - galaxy_pos[j][0]) + abs(galaxy_pos[i][1] -
                galaxy_pos[j][1])
        print(f"{galaxy_pos[i]=}")
        print(f"{galaxy_pos[j]=}")
        for e_i in empty_i:
            if galaxy_pos[i][0] <= e_i and e_i <= galaxy_pos[j][0]:
                all_galaxy_paths[(i, j)] += (num_inc - 1)
            if galaxy_pos[j][0] <= e_i and e_i <= galaxy_pos[i][0]:
                all_galaxy_paths[(i, j)] += (num_inc - 1)
        for e_j in empty_j:
            if galaxy_pos[i][1] <= e_j and e_j <= galaxy_pos[j][1]:
                all_galaxy_paths[(i, j)] += (num_inc - 1)
            if galaxy_pos[j][1] <= e_j and e_j <= galaxy_pos[i][1]:
                all_galaxy_paths[(i, j)] += (num_inc - 1)


print(sum(all_galaxy_paths.values()))
