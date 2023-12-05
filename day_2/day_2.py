import re

f = open("day_2\input.txt", "r")
lines = f.readlines()

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}
sum = 0

def all_pass(games: []):
    for game in games:
        balls = game.split(",")
        for ball in balls:
            num, color = ball.strip().split(' ')
            if int(num) > limits[color]:
                return False
    
    return True

for line in lines:
     group, game = line.split(":")
     gr_num = int(re.search(r'\d+', group).group())
     games = game.strip().split(";")
     if all_pass(games):
         sum = sum+gr_num
     
print(sum)

#part 2

def get_power(games: []):
    iteration = {
        "red": [],
        "green": [],
        "blue": []
    }
    
    for game in games:
        balls = game.split(",")
        for ball in balls:
            num, color = ball.strip().split(' ')
            iteration[color].append(int(num))
    
    return max(iteration["red"]) * max(iteration["green"]) * max(iteration["blue"])
    

sum = 0
for line in lines:
     group, game = line.split(":")
     gr_num = int(re.search(r'\d+', group).group())
     games = game.strip().split(";")
     sum = sum + get_power(games)
     
print(sum)