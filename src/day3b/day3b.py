# This code would have been nicer if I'd just read an array of strings instead of an array of arrays of chars.
width = 12
length = 1000
summary = [0] * width
data = [[0 for i in range(width)] for j in range(length)]

def common_char_at_pos(pos:int, default:str):
    value = 0
    for item in data:
        if int(item[pos]):
            value += 1
        else:
            value -= 1

    if value > 0:
        return '1'
    elif value < 0:
        return '0'
    else:
        return default


with open('/Users/eilidh/PycharmProjects/advent_of_code/src/day3/input.txt') as file:
    # read all into an array of arrays
    for i, line in enumerate(file):
        line = line.rstrip()
        if len(line) != width:
            raise Exception('wrong length')

        for j, char in enumerate(line.rstrip()):
            data[i][j] = char # realised later that I don't need a 2d array. An array of strings would have been fine.

original_data = data

i = 0
while len(data) > 1:
    common = common_char_at_pos(i, '1')
    keepers = []
    for thing in data:  # can't remove items from array while iterating - messes it up
        if thing[i] == common:
            keepers.append(thing)
    data = keepers
    i += 1

oxy =  int(''.join(keepers[0]), 2)
print(oxy)

data = original_data
i = 0
while len(data) > 1:
    common = common_char_at_pos(i, '1')
    keepers = []
    for thing in data:  # can't remove items from array while iterating - messes it up
        if thing[i] != common:
            keepers.append(thing)
    data = keepers
    i += 1

co2 =  int(''.join(keepers[0]), 2)
print(co2)

print('total')
print(co2 * oxy)