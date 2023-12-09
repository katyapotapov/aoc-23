with open("1_input.txt") as f:
    ls = f.readlines()

sum_nums = 0
for l in ls:
    for c in l:
        if c.isnumeric():
            first_num = c
            break

    for c in l[::-1]:
        if c.isnumeric():
            last_num = c
            break

    num = int(f"{first_num}{last_num}")
    sum_nums += num

print(sum_nums)
