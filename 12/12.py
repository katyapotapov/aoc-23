import math
from collections import Counter
import copy

with open("input.txt") as f:
    ls = f.readlines()

in_to_grp = []
for l in ls:
    in_str = l[:l.find(" ")]
    in_str = "?".join([in_str for i in range(5)])
    print(in_str)
    grps = [int(i) for i in l[l.find(" "):].strip().split(",")]
    grps = grps * 5
    print(grps)
    in_to_grp.append((in_str, tuple(grps)))

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
            last_combos = Counter([((), False)])
        else:
            last_combos = arr[i-1]
        if in_str[i] == "?":
            possible_chars = ".#"
        else:
            possible_chars = in_str[i]
        new_combos = Counter()
        for (combo, run), count in last_combos.most_common():
            for char in possible_chars:
                # print(f"{combo=}, {run=}, {char=}")
                if char == ".":
                    new_combos[(combo, False)] += count
                elif char == "#" and run:
                    new_combo = combo[:-1]
                    new_combo += ((combo[-1] + 1),)
                    new_combos[(new_combo, True)] += count
                elif char == "#" and not run:
                    this_combo = combo
                    this_combo += (1,)
                    new_combos[(this_combo, True)] += count

        actual_combos = Counter()
        for (combo, run), count in new_combos.most_common():
            if len(combo) > len(grp):
                continue
            broken = False
            for j in range(len(combo)):
                if combo[j] > grp[j] or (j < len(combo)-1 and combo[j] < grp[j]):
                    broken = True
                    break
            if broken:
                continue
            actual_combos[(tuple(combo), run)] += count
        # print(f"{actual_combos=}")

        arr.append(actual_combos)

    # print(f"{in_str=}")
    # print(f"{grp=}")
    # print(f"{arr[-1]=}")


    # now check
    print("checkiNg")
    for (check_grp, _ ), cnt in arr[-1].most_common():
        print(f"{check_grp=}")
        print(f"{grp=}")
        if check_grp == grp:
            print(f"{cnt=}")
            perms += cnt

print(perms)


