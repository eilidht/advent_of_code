
length = 12
summary = [0] * length
mask = '1' * length

with open('/Users/eilidh/PycharmProjects/advent_of_code/src/day3/input.txt') as file:
    for line in file:
        line = line.rstrip()
        if len(line) != length:
            raise Exception('wrong length')

        for i, char in enumerate(line.rstrip()):
            if int(char):
                summary[i] += 1
            else:
                summary[i] -= 1

print(summary)

bin_str = ''
for value in summary:
    if value > 0:
        bin_str += '1'
    elif value < 0:
        bin_str += '0'
    else:
        raise Exception('behaviour unspecified')

print(bin_str)
gamma = int(bin_str, 2)
mask = int(mask, 2)
epsilon = gamma^mask
print(gamma)
print(epsilon)
print(f'final value: {gamma * epsilon}')