import re

# f = open("day_3\example.txt", "r")
f = open("day_3\input.txt", "r")
lines = f.readlines()
row = 0


def get_nums(line: str):
    return [(int(match.group()), match.start()) for match in re.finditer(r'\d+', line)]

def has_symbol(num, row, start, end):
    if row < 0 or row >= len(lines):
        return False
    
    line = lines[row].strip()
    line = line[start:end]
    if bool(re.search(r'[^0-9.]', line)):
        # print(f"num: {num} row: {row}  pos: {start} - {end} line: {line}")
        return True
    
    return False
    
sum = 0
for line in lines:
    nums = get_nums(line)
    for num in nums:
        start = max(0, num[1] - 1)
        end = min(num[1] + len(str(num[0]))+1, len(line))
        
        if has_symbol(num, row -1, start, end) or \
            has_symbol(num, row, start, end) or \
            has_symbol(num, row + 1, start, end):
            sum = sum + num[0]
    
    row = row + 1
    
print(sum)
# 498559

def get_nums_on_pos(row: int, pos: int):
    result = []
    if row < 0 or row >= len(lines):
        return result
    
    line = lines[row].strip()
    nums = get_nums(line)
    for num in nums:
        start = max(0, num[1] - 1)
        end = min(num[1] + len(str(num[0])), len(line))
        
        if pos >= start and pos <= end:
            result.append(num[0])
    
    return result
        
sum = 0
row = 0
for line in lines:
    
    if "*" in line:
        for index in [match.start() for match in re.finditer(r'\*', line)]:
            nums = []
            nums = nums + get_nums_on_pos(row-1, index)
            nums = nums + get_nums_on_pos(row, index)
            nums = nums + get_nums_on_pos(row+1, index)
            
            if len(nums) == 2:
                print(nums)
                sum = sum + nums[0] * nums[1]
            elif len(nums) == 3:
                print(f"3 numbers!! {nums}")

    row = row + 1
print(sum)
#72246648