import re

f = open("day_5\example.txt", "r")
# f = open("day_5\input.txt", "r")
lines = f.readlines()
lines = [s.strip() for s in lines if s != '\n']
num_lines = len(lines)

def get_nums(line: str):
    return [int(match.group()) for match in re.finditer(r'\d+', line)]

seeds = get_nums(lines[0])

maps = []
arr = []
for line in lines[1:]:
    if line[0].isalpha():
        if len(arr) > 0:
            arr.sort()
            maps.append(arr)
        arr = []
        continue
    (source, dest, size) = get_nums(line)
    arr.append((source, dest, size))
    
arr.sort()
maps.append(arr)

# print(maps)

result = []

def get_destination(arr, seed):
    for pos in arr:
        if seed >= pos[1] and seed < pos[1] + pos[2]:
            return seed + pos[0] - pos[1]
        
    return seed

for seed in seeds:
    dest = seed
    for lists in maps:
        dest = get_destination(lists, dest)
    
    result.append((dest, seed))
    
    
result.sort()
print(result)
print("#### part 2 ####")
#part 2
location = None
# new_seeds = set()
# for seed_idx in range(int(len(seeds)/2)):
#     for idx in range(seeds[(seed_idx * 2) + 1]):
#         seed = seeds[seed_idx * 2] + idx
#         new_seeds.add(seed)
        
# new_seeds = list(new_seeds)
# new_seeds.sort()
#  

for seed_idx in range(int(len(seeds)/2)):
    for idx in range(seeds[(seed_idx * 2) + 1]):
        seed = seeds[seed_idx * 2] + idx
        dest = seed
        for lists in maps:
            dest = get_destination(lists, dest)
        
        print((seed, dest))
        if location is None or dest < location:
            location = dest
            print(location)


# for seed in new_seeds:
#     dest = seed
#     for lists in maps:
#         dest = get_destination(lists, dest)
        
#     if location is None or dest < location:
#         location = dest
#         print(location)
    
    
print(location)
#3987572099