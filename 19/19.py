import re
import sys
sys.setrecursionlimit(10000)


# with open("input_long.txt") as f:
with open("input.txt") as f:
    ls = f.readlines()

wfs = {}
for l in ls:
    if l == "\n":
        break
    wfs[l[:l.find("{")]] = l[l.find("{")+1:l.find("}") ]

import dataclasses
@dataclasses.dataclass
class Node:
    prev: "Node"
    val: str
    cond: bool | None = None

accepted_nodes = []
def create_node(wfs, wf_name, prev, cond=None):
    orig_prev = prev
    if wf_name == "R" or wf_name == "A":
        return Node(prev, wf_name, cond=cond)
    steps = wfs[wf_name].split(",") 
    for i, step in enumerate(steps):
        if step == "R" or step == "A":
            return Node(prev, wf_name, cond=cond)
        elif ":" in step:
            prev = Node(prev, step[:step.find(":")], cond=cond)
            other = create_node(wfs, step[step.find(":")+1:], prev, cond=True)
            if other.val == "A":
                accepted_nodes.append(other)
        else:
            prev = create_node(wfs, step, prev, cond=False)
            if prev.val == "A":
                accepted_nodes.append(prev)
    if prev == orig_prev:
        raise Exception()
    return prev

nodes = create_node(wfs, "in", None)

def bt(node):
    node_info = (node.val, node.cond)
    if node.prev is None:
        return node_info
    return node_info + bt(node.prev)

def get_accepted_paths(accepted_nodes):
    accepted_paths = []
    for node in accepted_nodes:
        accepted_paths.append(bt(node))
    return accepted_paths

accepted_paths = get_accepted_paths(accepted_nodes)
# print(accepted_paths)

ranges = []

def init_acceptable_range():
    acceptable_range = {}
    for c in ["x", "m", "a", "s"]:
        acceptable_range[f"{c}_min"] = 1
        acceptable_range[f"{c}_max"] = 4000
    return acceptable_range

for path in accepted_paths:
    if path[0] != "A":
        raise Exception()
    if path[-1] is not None:
        print(f"We expected path[-1] to be None but it's actually{path[-1]}")

    path = path[1:-1]

    acceptable_range = init_acceptable_range()
    for i in range(0, len(path), 2):
        res = path[i]
        cond = path[i+1]

        if "<" in cond:
            r = cond[:cond.find("<")]
            val = int(cond[cond.find("<")+1:cond.find(":")])
            dest = cond[cond.find(":")+1:]
        elif ">" in cond:
            r = cond[:cond.find(">")]
            val = int(cond[cond.find(">")+1:cond.find(":")])
            dest = cond[cond.find(":")+1:]
        else:
            raise Exception()

        if "<" in cond and not res:
            lim = f"{r}_min"
            acceptable_range[lim] = max(acceptable_range[lim], val)
        elif "<" in cond and res:
            lim = f"{r}_max"
            acceptable_range[lim] = min(acceptable_range[lim], val-1)
        elif ">" in cond and not res:
            lim = f"{r}_max"
            acceptable_range[lim] = min(acceptable_range[lim], val)
        elif ">" in cond and res:
            lim = f"{r}_min"
            acceptable_range[lim] = max(acceptable_range[lim], val+1)
        else:
            raise Exception()

    ranges.append(acceptable_range)

[print(r) for r in ranges]


actual_ranges = [ranges[0]]
# now we have to eliminate all the duplicate possibilities
for i in range(1, len(ranges)):
    for j in range(len(actual_ranges)):
        contiguous = True
        for c in ["x", "m", "a", "s"]:
            c_min = f"{c}_min"
            c_max = f"{c}_max"
            if not (ranges[i][c_max] >= actual_ranges[j][c_min] and
                    actual_ranges[j][c_max] >= ranges[i][c_min]):
                contiguous = False
                break
        if not contiguous:
            continue

        # otherwise the ranges are overlapping so we can just merge them
        for c in ["x", "m", "a", "s"]:
            c_min = f"{c}_min"
            c_max = f"{c}_max"

            actual_ranges[j][c_min] = min(actual_ranges[j][c_min], ranges[i][c_min])
            actual_ranges[j][c_max] = max(actual_ranges[j][c_max], ranges[i][c_max])
    if j == len(actual_ranges):
        actual_ranges.append(ranges[i])



# [print(r) for r in actual_ranges]

total_opts = 0
for rng in actual_ranges:
    invalid_range = False
    current_opts = 1
    for c in ["x", "m", "a", "s"]:
        c_min = rng[f"{c}_min"]
        c_max = rng[f"{c}_max"]
        if c_min > c_max:
            invalid_range = True
            break
        current_opts *= (c_max - c_min)

    if not invalid_range:
        total_opts += current_opts
print(total_opts)

