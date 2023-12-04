import os

f = open("day_1\input.txt", "r")
lines = f.readlines()
sum = 0
for line in lines:
    digits = [char for char in line if char.isdigit()]
    num = int(str(digits[0]) + str(digits[-1]))
    # print(num)
    sum = sum + num

print(sum)
# 54601

nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def find_all_indexes(input_str, substring):
    l2 = len(substring)
    return [i for i in range(len(input_str)) if input_str[i : i + l2] == substring]


def get_nums(line: str):
    arr = []
    for k in nums:
        if k in line:
            ids = find_all_indexes(line, k)
            for id in ids:
                arr.append((id, nums[k]))

    return arr


sum = 0
for line in lines:
    line_nums = get_nums(line)
    line_nums = sorted(line_nums, key=lambda x: x[0])
    num = int(str(line_nums[0][1]) + str(line_nums[-1][1]))
    sum = sum + num

print(sum)
# 54078
