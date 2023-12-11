import re

# f = open("day_6\example.txt", "r")
f = open("day_6\input.txt", "r")
lines = f.readlines()

def get_nums(line: str):
    return [int(match.group()) for match in re.finditer(r'\d+', line)]

times = get_nums(lines[0])
distances = get_nums(lines[1])

def calc_result(times, distances):
    result = 1
    for idx in range(0, len(times)):
        time = times[idx]
        race_distance = distances[idx]
        count = 0
        for ms in range(1, time): 
            distance = ms * (time - ms)
            if distance > race_distance:
                count = count + 1
        if count > 0:
            result = result * count
    
    
    print (result)

calc_result(times, distances)


times = get_nums(lines[0].replace(" ", ""))
distances = get_nums(lines[1].replace(" ", ""))
calc_result(times, distances)
