import re
import math

# f = open("day_8\example.txt", "r")
# f = open("day_8\example2.txt", "r")
# f = open("day_8\example3.txt", "r")
f = open("day_8\input.txt", "r")
lines = f.readlines()

order = [int(item) for item in lines[0].strip().replace("R", "1").replace("L", "0")]
default_order = [1, 0]

pos_map = {}
for line in lines[2:]:
    pos = line[0:3]
    left = line[7:10]
    right = line[12:15]
    pos_map[pos] = (left, right)
    
pos = 0
val = "AAA"
count = len(order)
while val != "ZZZ":
    idx = order[pos % count]
    pos = pos + 1
    # prev_val = val
    val = pos_map[val][idx]
    
    print(f"pos: {pos}. idx: {idx} from {prev_val} to {val}")


vals = [val for val in pos_map.keys() if val[2] == 'A']


pos = 0
all = False

all_pos = []

for val in vals:
    pos = 0
    while val[2] != "Z":
        idx = order[pos % count]
        pos = pos + 1
        # prev_val = val
        val = pos_map[val][idx]
        
        # print(f"pos: {pos}. idx: {idx} from {prev_val} to {val}")
    print(f"val: {val}, pos: {pos}")
    all_pos.append(pos)

result = 1
for pos in all_pos:
    result = result * pos

def find_lcm(num1, num2):
   return (num1*num2) // math.gcd(num1,num2)

def find_lcm_for_list(lst):
   num1 = lst[0]
   num2 = lst[1]
   lcm = find_lcm(num1, num2)

   for i in range(2, len(lst)):
       lcm = find_lcm(lcm, lst[i])

   return lcm

print(find_lcm_for_list(all_pos))