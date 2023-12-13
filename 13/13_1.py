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

def check_mirror(pttn):
    is_mirror = True
    for j in range(min(i, len(pttn)-i)):
        # print(f"{pttn[i-j-1]=}")
        # print(f"{pttn[i+j]=}")
        if pttn[i-j-1] != pttn[i+j]:
            is_mirror = False
            break
    if is_mirror:
        return i


# horizontal
row_matches = 0
for pttn in pttns:
    for i in range(1, len(pttn)):
        if pttn[i] == pttn[i-1]:
            maybe_match = check_mirror(pttn)
            if maybe_match:
                row_matches += maybe_match

for i in range(len(pttns)):
    pttns[i] = np.array(pttns[i]).T.tolist()
    print(f"{pttns[i]=}")

col_matches = 0
for pttn in pttns:
    for i in range(1, len(pttn)):
        if pttn[i] == pttn[i-1]:
            maybe_match = check_mirror(pttn)
            if maybe_match:
                col_matches += maybe_match

print(col_matches)
print(row_matches)
print(col_matches + row_matches * 100)
