with open("input.txt") as f:
    ls = f.readlines()

sum_wins = 0
for l in ls:
    w = [int(i) for i in l[l.find(":")+1:l.find("|")].strip().split()]
    h = [int(i) for i in l[l.find("|")+1:].strip().split()]

    h_w = [i for i in w if i in h]
    f = 1
    tot = 0
    for i in h_w:
        if tot == 0:
            tot = 1
        else:
            tot *= 2

    sum_wins += tot

print(sum_wins)
