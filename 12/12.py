import re
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

for in_str, grp in in_to_grp:
    # print(len(re.findall(f'[?.]+[?#]{1}[?.]+[?#]{1}[?.]+[?#]{3}', in_str)))
    print(len(re.findall(f'[?.]+', in_str)))

