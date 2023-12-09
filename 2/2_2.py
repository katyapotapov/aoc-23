import re

with open("input.txt") as f:
    ls = f.readlines()

sum_powers = 0

for l in ls:
    game_id = int(l[5:l.find(":")])

    num_red = max([int(num) for num in re.findall(f'([0-9]+?) red', l)])
    num_green = max([int(num) for num in re.findall(f'([0-9]+?) green', l)])
    num_blue = max([int(num) for num in re.findall(f'([0-9]+?) blue', l)])
    
    sum_powers += num_red * num_green * num_blue

print(sum_powers)
