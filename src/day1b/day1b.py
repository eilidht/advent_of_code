
previous = 100000
increased = 0

with open('/Users/eilidh/PycharmProjects/advent_of_code/src/day1b/input.txt') as file:
    lines = file.readlines()
    lines = [int(line) for line in lines]
    for i in range(len(lines)-3):
        slice1 = lines[i:i+3]
        slice2 = lines[i+1:i+4]
        print(f'{slice1}, {sum(slice1)}')
        print(f'{slice2}, {sum(slice2)}')
        if sum(slice2) > sum(slice1):
            print('increased')
            increased += 1
        else:
            print('not increased')

print("increased: ")
print(increased)