import re

with open("input_long.txt") as f:
    ls = f.readlines()

inst = []
for l in ls:
    inst.append((l[0], int(l[l.find(" ")+1:l.find("(")-1])))


size_i = 500
size_j = 600
lag = [[0 for _ in range(size_j)] for _ in range(size_i)]

start_pos = (150, 100)
cur_pos = start_pos
from collections import defaultdict
row_to_d = defaultdict(int)
d = (0, 0)
lag[cur_pos[0]][cur_pos[1]] = 1
for i in inst:
    if i[0] == "R":
        d = (0, 1)
    elif i[0] == "L":
        d = (0, -1)
    elif i[0] == "U":
        d = (-1, 0)
    elif i[0] == "D":
        d = (1, 0)
    else:
        raise Exception()
    
    row_to_d[cur_pos[0]] += d[0]
    for t in range(i[1]):
        cur_pos = (cur_pos[0] + d[0], cur_pos[1] + d[1])
        lag[cur_pos[0]][cur_pos[1]] = 1

[print(l) for l in lag]
    
edge_sum = (sum([sum(l) for l in lag]))

# nn
start = (start_pos[0]+1, start_pos[1])

fr = [start]
seen = []

from PIL import Image
import numpy as np

# Convert the array to a numpy array and scale it to 255 (for black and white)
image_data = np.array(lag) * 255

# Create an image object
image = Image.fromarray(np.uint8(image_data), 'L')

# Save or show the image
image.save('output_img.png')

fill = 0
for i in range(len(lag)):
    for j in range(len(lag[0])):
        if lag[i][j] == 1:
            continue
        ds_i = row_to_d[i]
        if j != 0 and (sum(lag[i][:j]) + abs(ds_i)) % 2 == 1:
            fill += 1
while len(fr) > 0:
    n = fr.pop()
    if n in seen:
        continue
    seen.append(n)
    if lag[n[0]][n[1]] == 0:
        fill += 1

    if n[1] > 0 and (n[0], n[1]-1) not in seen:
        fr.append((n[0], n[1]-1))
    if n[0] > 0 and (n[0]-1, n[1]) not in seen:
        fr.append((n[0]-1, n[1]))
    if n[1] < len(lag[0])-1 and (n[0], n[1]+1) not in seen:
        fr.append((n[0], n[1]+1))
    if n[0] < len(lag)-1 and (n[0]+1, n[1]) not in seen:
        fr.append((n[0]+1, n[1]))


print(edge_sum)
print(fill+edge_sum)

