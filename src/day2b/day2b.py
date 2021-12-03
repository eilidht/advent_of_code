hozpos = 0
depth = 0
aim = 0
with open('/Users/eilidh/PycharmProjects/advent_of_code/src/day2/input.txt') as file:
    for line in file:
        values = line.rstrip().split()
        if values[0] == 'down':
            aim += int(values[1])
        if values[0] == 'up':
            aim -= int(values[1])
        if values[0] == 'forward':
            # It increases your horizontal position by X units.
            hozpos += int(values[1])
            # It increases your depth by your aim multiplied by X.
            depth += aim * int(values[1])

print(f'horizontal position: {hozpos}')
print(f'depth: {depth}')
print(f'multiplied: {depth*hozpos}')