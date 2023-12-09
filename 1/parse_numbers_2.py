import re

with open("1_input.txt") as f:
    ls = f.readlines()

sum_nums = 0
string_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for i in range(1, 10):
    string_nums.append(str(i))

for l in ls:
    print(f"{l=}")
    first_num_ind = 1000000000000000
    last_num_ind = -1
    for i in range(len(string_nums)):
        ind = l.find(string_nums[i])
        # print(f"{ind=}, {string_nums[i]=}")
        if ind >= 0 and ind < first_num_ind:
            first_num_ind = ind
            first_num = i % 9 + 1

        ind = l.rfind(string_nums[i])
        if ind >= 0 and ind > last_num_ind:
            last_num_ind = ind
            last_num = i % 9 + 1

    print(f"{first_num=}")
    print(f"{last_num=}")
    num = first_num * 10 + last_num
    print(f"{num=}")
    sum_nums += num

print(sum_nums)
