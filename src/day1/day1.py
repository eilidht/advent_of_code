
previous = 100000
increased = 0
with open('/Users/eilidh/PycharmProjects/advent_of_code/src/day1/input.txt') as file:
    for line in file:
        print(line.rstrip())
        current = int(line)
        if current > previous:
            increased += 1
            print('increased')
        previous = current

print("increased: ")
print(increased)