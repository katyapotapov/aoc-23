import re
import numpy as np
from collections import OrderedDict


with open("input.txt") as f:
    ls = f.readlines()

insts = ls[0].split(",")

def get_label(inst):
    return ''.join(ch for ch in inst if ch.isalpha())

def get_hash(inst):
    cur_val = 0
    print(inst)
    for c in inst.strip():
        cur_val += (ord(c))
        cur_val *= 17
        cur_val %= 256
    return cur_val

boxes = [{} for i in range(256)]
for inst in insts:
    inst = inst.strip()
    lbl = get_label(inst)
    hsh = get_hash(lbl)
    if "-" in inst:
        if lbl in boxes[hsh]:
            del boxes[hsh][lbl]
    if "=" in inst:
        f_len = int(inst[inst.find("=")+1:])
        boxes[hsh][lbl] = f_len

print(boxes)

tot = 0
for i, box in enumerate(boxes):
    for j, (lbl, f_len) in enumerate(box.items()):
        print(lbl)
        pwr = (i+1) * (j+1) * f_len
        print(pwr)
        tot += pwr

print(tot)
