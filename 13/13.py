import re
import numpy as np

with open("input.txt") as f:
    ls = f.readlines()

pttns = []
cur_pttn = []
for l in ls:
    if l == "\n":
        pttns.append(cur_pttn)
        cur_pttn = []
    else:
        cur_pttn.append(list(l.strip()))

pttns.append(cur_pttn)

def check_line_mistakes(pttn, one, two):
    line_mistakes = []
    for c in range(len(pttn[0])):
        if pttn[one][c] != pttn[two][c]:
            line_mistakes.append(c)
    return line_mistakes

def check_mirror(pttn, i):
    mistakes = []
    for j in range(min(i, len(pttn)-i)):
        # print(f"{pttn[i-j-1]=}")
        # print(f"{pttn[i+j]=}")
        if pttn[i-j-1] != pttn[i+j]:
            mistakes.append((i-j-1, i+j))
    print(f"{mistakes=}")
    if len(mistakes) == 1:
        line_mistakes = check_line_mistakes(pttn, mistakes[0][0], mistakes[0][1])
        if len(line_mistakes) == 1:
            return i


# horizontal
row_matches = 0
for num_pttn, pttn in enumerate(pttns):
    print(f"{num_pttn=}")
    for i in range(1, len(pttn)):
        maybe_match = check_mirror(pttn, i)
        if maybe_match:
            row_matches += maybe_match
            print(f"row: {maybe_match=}")

for i in range(len(pttns)):
    pttns[i] = np.array(pttns[i]).T.tolist()

col_matches = 0
for num_pttn, pttn in enumerate(pttns):
    print(f"{num_pttn=}")
    for i in range(1, len(pttn)):
        maybe_match = check_mirror(pttn, i)
        if maybe_match:
            col_matches += maybe_match
            print(f"col: {maybe_match=}")

print(col_matches)
print(row_matches)
print(col_matches + row_matches * 100)
