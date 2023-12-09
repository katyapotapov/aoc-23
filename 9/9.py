with open("input.txt") as f:
    ls = f.readlines()

sum_diffs = 0
for l in ls:
    a = [int(x) for x in l.split()]
    diffs = [a[::-1]]

    while True:
        all_diffs_0 = len(diffs[-1]) == len([i for i in diffs[-1] if i == 0])
        if all_diffs_0:
            break

        diffs.append([])

        for i in range(1, len(diffs[-2])):
            diffs[-1].append(diffs[-2][i]-diffs[-2][i-1])


    for i in range(len(diffs)-1, 0, -1):
        diffs[i-1].append(diffs[i][-1] + diffs[i-1][-1])

    print(diffs)

    sum_diffs += diffs[0][-1]

print(sum_diffs)
