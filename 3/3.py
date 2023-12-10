import re

with open("input.txt") as f:
    ls = f.readlines()

# print(set(''.join(ls)))

from collections import defaultdict
num_pos = defaultdict(list)
for i in range(len(ls)):
    num_pos[i] += [(m.start(0), m.end(0)) for m in re.finditer(f'([0-9]+)', ls[i])]

gear_pos = []
for i in range(len(ls)):
    gear_pos += [(i, j.start()) for j in re.finditer(f'([*])', ls[i])]

print(gear_pos)
print(num_pos)

part_nums = defaultdict(list)

sum_ratios = 0

import copy
for (i, j) in gear_pos:
    num_pos_tmp = copy.deepcopy(num_pos)
    num_gears = 0
    gear_ratio = 1
    for i_i in range(max(0, i-1), min(len(ls), i+2)):
        for j_j in range(max(0, j-1), min(len(ls), j+2)):
            for b, e in num_pos_tmp[i_i]:
                if j_j >= b and j_j < e:
                    num_pos_tmp[i_i].remove((b, e))
                    num_gears += 1
                    gear_ratio *= int(ls[i_i][b:e])
                    break

    if num_gears == 2:
        sum_ratios += gear_ratio

print(sum_ratios)
