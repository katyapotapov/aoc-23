import re
import math
import copy

with open("input.txt") as f:
    ls = f.readlines()

in_to_grp = []
for l in ls:
    in_str = l[:l.find(" ")]
    grps = [int(i) for i in l[l.find(" "):].strip().split(",")]
    in_to_grp.append((in_str, grps))

print(in_to_grp)
import itertools

perms = 0
opts = "#."
for in_str, grp in in_to_grp:
    in_str = list(in_str)
    all_combos = itertools.product(opts, repeat=in_str.count("?"))

    for combo in all_combos:
        cur_q = 0
        new_str = copy.deepcopy(in_str)
        for i in range(len(new_str)):
            if new_str[i] == "?":
                new_str[i] = combo[cur_q]
                cur_q += 1

        # now check
        check_grp = [len(list(group)) for key, group in itertools.groupby(new_str) if key == "#"]
        if check_grp == grp:
            perms += 1

print(perms)


