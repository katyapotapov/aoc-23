import math
import copy

with open("input.txt") as f:
    ls = f.readlines()

in_to_grp = []
for l in ls:
    in_str = l[:l.find(" ")]
    in_str = in_str * 5
    print(in_str)
    grps = [int(i) for i in l[l.find(" "):].strip().split(",")]
    grps = grps * 5
    print(grps)
    in_to_grp.append((in_str, grps))

import itertools
from functools import cache

@cache
def check_str(stri):
    grps = []
    in_grp = False
    for i in stri:
        if not in_grp and i == ".":
            continue
        elif not in_grp and i == "#":
            in_grp = True
            grps.append(1)
        elif in_grp and i == ".":
            in_grp = False
        elif in_grp and i == "#":
            grps[-1] += 1
    return grps

    # return [len(list(group)) for key, group in itertools.groupby(stri) if key == "#"]

perms = 0
for in_str, grp in in_to_grp:
    # print(f"{grp=}")
    arr = []
    in_str = list(in_str)
    # all_combos = itertools.product(opts, repeat=in_str.count("?"))

    # print("".join(in_str))
    for i in range(len(in_str)):
        if i == 0:
            last_combos = [([], False)]
        else:
            last_combos = arr[i-1]
        if in_str[i] == "?":
            possible_chars = ".#"
        else:
            possible_chars = in_str[i]

        new_combos = []
        for combo, run in last_combos:
            for char in possible_chars:
                # print(f"{combo=}, {run=}, {char=}")
                if char == ".":
                    new_combos.append((combo.copy(), False))
                elif char == "#" and run:
                    new_combo = combo[:-1].copy()
                    new_combo.append(combo[-1] + 1)
                    new_combos.append((new_combo, True))
                elif char == "#" and not run:
                    this_combo = combo.copy()
                    this_combo.append(1)
                    new_combos.append((this_combo, True))

        actual_combos = []
        for combo, run in new_combos:
            if len(combo) > len(grp):
                continue
            broken = False
            for j in range(len(combo)):
                if combo[j] > grp[j] or (j < len(combo)-1 and combo[j] < grp[j]):
                    broken = True
                    continue
            if broken:
                continue
            actual_combos.append((combo, run))
        # print(f"{actual_combos=}")

        arr.append(actual_combos)

    # print(f"{in_str=}")
    # print(f"{grp=}")
    # print(f"{arr[-1]=}")


    # now check
    cur_perms = 0
    print("checkiNg")
    for check_grp, _ in arr[-1]:
        if check_grp == grp:
            perms += 1
            cur_perms += 1

    print(cur_perms)

print(perms)


