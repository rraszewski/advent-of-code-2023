import re

# f = open("day_4\example.txt", "r")
f = open("day_4\input.txt", "r")
lines = f.readlines()
num_lines = len(lines)

def get_nums(line: str):
    return [int(match.group()) for match in re.finditer(r'\d+', line)]

def get_common_for_line(row):
    if row > num_lines:
        return set()
    line = lines[row]
    (bet, win) = line.strip().split(":")[1].split(("|"))
    bet_nums = set(get_nums(bet))
    win_nums = set(get_nums(win))
    return bet_nums & win_nums

row = 0
total_points = 0
result=[0] * num_lines
for line in lines:
    score = 0
    common = get_common_for_line(row)
    
    result[row] = result[row] + 1
    
    if len(common) > 0:
        score = 2 ** (len(common) -1)
        total_points = total_points + score
    
    row = row +1
        
print(total_points)
#20117

# part 2

row = 0
result=[1] * num_lines
for line in lines:
    common = get_common_for_line(row)
    if len(common) > 0:
        for i in range(len(common)):
            if (row + i) < (num_lines - 1):
                result[row + i +1] = result[row + i + 1] + result[row]
    row = row + 1
print(sum(result))