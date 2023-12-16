import re

with open("input.txt") as f:
    ls = f.readlines()

for i in range(len(ls)):
    ls[i] = list(ls[i].strip())

largest_so_far = 0
for bs_i in range(70, len(ls + ls[0])):
    if bs_i < len(ls):
        bs = [(bs_i, 0)]
        b_dirs = [(0, 1)]
    else:
        bs = [(0, bs_i - len(ls))]
        b_dirs = [(1, 0)]

    ener = [[0 for l in ls[0]] for i in ls]

    # allowable_iter = 800
    allowable_iter = 1000
    itr = 0
    while len(bs) > 0:
        maybe_bs = []
        maybe_b_dirs = []
        for i in range(len(bs)):
            b = bs[i]
            b_dir = b_dirs[i]
            ener[b[0]][b[1]] = 1
            cur_sym = ls[b[0]][b[1]]
            if cur_sym == ".":
                pass
            elif cur_sym == "/":
                b_dirs[i] = (-b_dir[1], -b_dir[0])
            elif cur_sym == "\\":
                b_dirs[i] = (b_dir[1], b_dir[0])
            elif cur_sym == "|" and b_dir[1] == 0:
                pass
            elif cur_sym == "-" and b_dir[0] == 0:
                pass
            elif cur_sym == "|" and b_dir[1] != 0:
                b_dirs[i] = (1, 0)
                maybe_bs.append(b)
                maybe_b_dirs.append((-1, 0))
            elif cur_sym == "-" and b_dir[0] != 0:
                b_dirs[i] = (0, 1)
                maybe_bs.append(b)
                maybe_b_dirs.append((0, -1))

            bs[i] = (bs[i][0] + b_dirs[i][0], bs[i][1] + b_dirs[i][1])

        new_bs = []
        new_b_dirs = []
        for i in range(len(bs)):
            if bs[i][0] < len(ls) and bs[i][1] < len(ls[0]) and bs[i][0] >= 0 and bs[i][1] >= 0:
                new_bs.append(bs[i])
                new_b_dirs.append(b_dirs[i])
        for i in range(len(maybe_bs)):
            if maybe_bs[i][0] < len(ls) and maybe_bs[i][1] < len(ls[0]) and maybe_bs[i][0] >= 0 and maybe_bs[i][1] >= 0:
                new_bs.append(maybe_bs[i])
                new_b_dirs.append(maybe_b_dirs[i])

        bs = new_bs
        b_dirs = new_b_dirs
        # print(bs)
        # print(b_dirs)

        itr += 1
        if itr > allowable_iter:
            break


        
    # [print(_) for _ in ener]

    
    sm = (sum([sum(e) for e in ener]))
    print(f"{bs_i=}")
    print(f"{sm=}")
    largest_so_far = max(largest_so_far, sm)
    print(f"{largest_so_far=}")
