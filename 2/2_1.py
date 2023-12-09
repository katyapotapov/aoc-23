import re

with open("input.txt") as f:
    ls = f.readlines()

sum_game_ids = 0

for l in ls:
    game_id = int(l[5:l.find(":")])

    num_red = max([int(num) for num in re.findall(f'([0-9]+?) red', l)])
    num_green = max([int(num) for num in re.findall(f'([0-9]+?) green', l)])
    num_blue = max([int(num) for num in re.findall(f'([0-9]+?) blue', l)])
    
    if num_red > 12 or num_green > 13 or num_blue > 14:
        continue

    sum_game_ids += game_id

print(sum_game_ids)
