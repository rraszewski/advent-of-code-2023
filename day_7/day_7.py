import re

# f = open("day_7\example.txt", "r")
f = open("day_7\input.txt", "r")
lines = f.readlines()

value_map = {
    'T': 'A',
    'J': 'B',
    'Q': 'C',
    'K': 'D',
    'A': 'E',
}


def get_val_str(vals_str, vals_set, jokers = 0):
    if len(vals_set) == 1:
        return  '6' + vals_str
    elif len(vals_set) == 2:
        cnt= list(vals_set.values())[0]
        if cnt + jokers == 4 or cnt == 1:
            return  '5' + vals_str
        else:
            return  '4' + vals_str
    elif len(vals_set) == 3:
        for val in vals_set.keys():
            if vals_set[val] + jokers == 3:
                return  '3' + vals_str
        return  '2' + vals_str
    elif len(vals_set) == 4:
        return  '1' + vals_str
    elif len(vals_set) == 5:
        return '0' + vals_str
    elif len(vals_set) == 0:
        return  '6' + vals_str #only jokers!

def count_value(vals:[]):
    vals_str = ''.join(vals)
    vals_set = {}
    for ch in vals:
        val = vals_set.get(ch, 0)
        vals_set[ch] = val + 1

    return get_val_str(vals_str, vals_set)

def count_value2(vals:[]):
    vals_str = ''.join(vals)
    vals_set = {}
    for ch in vals:
        val = vals_set.get(ch, 0)
        vals_set[ch] = val + 1
    jokers = vals_set.get('1', 0)
    if jokers:
        del vals_set['1'] # remove all jokers
        
    return get_val_str(vals_str, vals_set, jokers)


mapped_bids = []
for line in lines:
    hand, bid = line.split(' ')
    hand_result = [value_map.get(ch, ch) for ch in hand]
    
    value = count_value(hand_result)
    mapped_bids.append((value, hand, int(bid)))
    
mapped_bids.sort()
result = 0
for idx in range(0, len(mapped_bids)):
    result = result + (idx + 1) * mapped_bids[idx][2]
    
    
print(result)


# part 2
value_map = {
    'T': 'A',
    'J': '1',
    'Q': 'C',
    'K': 'D',
    'A': 'E',
}


mapped_bids = []
for line in lines:
    hand, bid = line.split(' ')
    hand_result = [value_map.get(ch, ch) for ch in hand]
    
    value = count_value2(hand_result)
    mapped_bids.append((value, hand, int(bid)))
    
mapped_bids.sort()
result = 0
for idx in range(0, len(mapped_bids)):
    result = result + (idx + 1) * mapped_bids[idx][2]
    
print(result)
