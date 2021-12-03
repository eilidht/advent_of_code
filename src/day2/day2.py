hozpos = 0
depth = 0
with open('/Users/eilidh/PycharmProjects/advent_of_code/src/day2/test_input.txt') as file:
    for line in file:
        values = line.rstrip().split()
        if values[0] == 'forward':
            hozpos += int(values[1])
        if values[0] == 'down':
            depth += int(values[1])
        if values[0] == 'up':
            depth -= int(values[1])

print(f'horizontal position: {hozpos}')
print(f'depth: {depth}')
print(f'multiplied: {depth*hozpos}')