import re
import numpy as np
import copy

with open("input.txt") as f:
    ls = f.readlines()

rocks = []
for l in ls:
    rocks.append(list(l.strip()))
# [i.reverse() for i in rocks]

# [print(str(i)) for i in rocks]
# rocks = np.rot90(np.array(rocks).tolist(), 2).tolist()

all_rocks = 0
prev_rocks = []
# cycles = 1000000000
cycles = 1000000000
for c in range(4 * cycles):
    # N
    if c % 4 == 0:
        # Cols are fixed
        for j in range(len(rocks[0])):
            anchor = 0
            pile_size = 0
            for i in range(len(rocks)):
                if rocks[i][j] == "O":
                    rocks[i][j] = "."
                    rocks[anchor+pile_size][j] = "O"
                    pile_size += 1
                elif rocks[i][j] == "#":
                    anchor = i+1
                    pile_size = 0
    # W
    elif c % 4 == 1:
        # Rows are fixed
        for i in range(len(rocks)):
            anchor = 0
            pile_size = 0
            for j in range(len(rocks[0])):
                if rocks[i][j] == "O":
                    rocks[i][j] = "."
                    rocks[i][anchor+pile_size] = "O"
                    pile_size += 1
                elif rocks[i][j] == "#":
                    anchor = j+1
                    pile_size = 0
    # # S
    elif c % 4 == 2:
        # Cols are fixed
        for j in range(len(rocks[0])):
            anchor = 0
            pile_size = 0
            for i in reversed(range(len(rocks))):
                if rocks[i][j] == "O":
                    rocks[i][j] = "."
                    rocks[anchor-pile_size][j] = "O"
                    pile_size += 1
                elif rocks[i][j] == "#":
                    anchor = i-1
                    pile_size = 0
    # # E
    elif c % 4 == 3:
        # Rows are fixed
        for i in range(len(rocks)):
            anchor = 0
            pile_size = 0
            for j in reversed(range(len(rocks[0]))):
                if rocks[i][j] == "O":
                    rocks[i][j] = "."
                    rocks[i][anchor-pile_size] = "O"
                    pile_size += 1
                elif rocks[i][j] == "#":
                    anchor = j-1
                    pile_size = 0

    if c % 4 == 3:
        total_w = 0
        # Cols are fixed
        for i in range(len(rocks)):
            cur_w = 0
            for j in range(len(rocks[0])):
                if rocks[i][j] == "O":
                    cur_w += (len(rocks) - i)
                    print(f"{i=}, {j=}: {cur_w=}")
            total_w += cur_w
        print(f"{total_w=}")



