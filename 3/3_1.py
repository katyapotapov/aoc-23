import re

with open("input.txt") as f:
    ls = f.readlines()

# print(set(''.join(ls)))

from collections import defaultdict
num_pos = defaultdict(list)
for i in range(len(ls)):
    num_pos[i] += [(m.start(0), m.end(0)) for m in re.finditer(f'([0-9]+)', ls[i])]

symbol_pos = []
for i in range(len(ls)):
    symbol_pos += [(i, j.start()) for j in re.finditer(f'([%$*#+&/@!=-])', ls[i])]

print(symbol_pos)
print(num_pos)

part_nums = defaultdict(list)

sum_parts = 0

for (i, j) in symbol_pos:
    for i_i in range(max(0, i-1), min(len(ls), i+2)):
        for j_j in range(max(0, j-1), min(len(ls), j+2)):
            for b, e in num_pos[i_i]:
                if j_j >= b and j_j < e:
                    num_pos[i_i].remove((b, e))
                    sum_parts += int(ls[i_i][b:e])
                    break

print(sum_parts)
