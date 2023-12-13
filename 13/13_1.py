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

# horizontal
row_matches = 0
for pttn in pttns:
    for i in range(1, len(pttn)):
        if pttn[i] == pttn[i-1]:
            # check the rest
            is_mirror = True
            for j in range(min(i, len(pttn)-i)):
                print(f"{j=}")
                # print(f"{pttn[i-j-1]=}")
                # print(f"{pttn[i+j]=}")
                if pttn[i-j-1] != pttn[i+j]:
                    is_mirror = False
                    break
            if is_mirror:
                row_matches += i
                print(f"row: {i=}")

for i in range(len(pttns)):
    pttns[i] = np.array(pttns[i]).T.tolist()
    print(f"{pttns[i]=}")

col_matches = 0
for pttn in pttns:
    for i in range(1, len(pttn)):
        if pttn[i] == pttn[i-1]:
            is_mirror = True
            for j in range(min(i, len(pttn)-i)):
                # print(f"{pttn[i-j-1]=}")
                # print(f"{pttn[i+j]=}")
                if pttn[i-j-1] != pttn[i+j]:
                    is_mirror = False
                    break
            if is_mirror:
                col_matches += i
                print(f"col: {i=}")

print(col_matches)
print(row_matches)
print(col_matches + row_matches * 100)
