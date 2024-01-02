from collections import defaultdict

with open("input.txt") as f:
    ls = f.readlines()

num_i = [1] * len(ls)
for l_ind in range(len(ls)):
    l = ls[l_ind]
    w = [int(i) for i in l[l.find(":")+1:l.find("|")].strip().split()]
    h = [int(i) for i in l[l.find("|")+1:].strip().split()]

    h_w = [i for i in w if i in h]
    tot = len(h_w)
    for num_i_ind in range(l_ind + 1, min(len(num_i), l_ind + tot + 1)):
        num_i[num_i_ind] += num_i[l_ind]

    print(f"Card {l_ind}")
    print(num_i)



print(sum(num_i))
