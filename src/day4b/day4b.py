
new_board = True
board = None
list_of_boards = []
with open('/Users/eilidh/PycharmProjects/advent_of_code/src/day4b/input.txt') as file:

    # read all into an array of arrays
    for i, line in enumerate(file):
        line = line.rstrip()
        if i==0:
            drawn_nos = line.split(',')
            drawn_nos = [int(x) for x in drawn_nos]
        else:
            if len(line) == 0:
                new_board = True
            else:
                if new_board:
                    new_board = False
                    board_row = 0
                    board = [[0 for k in range(len(line.split()))] for m in range(len(line.split()))]

                for board_col, char in enumerate(line.split()):
                    board[board_row][board_col] = int(char)
                board_row += 1
                if board_row == len(line.split()):
                    transposed_board = [[board[w][y] for w in range(len(board))] for y in range(len(board[0]))]
                    double_board = board + transposed_board

                    double_board_tuple = tuple(tuple(i) for i in double_board)
                    list_of_boards.append(double_board_tuple)

print(drawn_nos)
print(list_of_boards)

winning_boards = set()
last_board = None

for i in range(5,len(drawn_nos)):
    if len(winning_boards) < (len(list_of_boards)-1):
        already_drawn = drawn_nos[0:i]
        print(already_drawn)
        for b in list_of_boards:
            for row in b:
                if set(row).issubset(already_drawn):
                    print(row)
                    print('matches')
                    winning_boards.add(b)

for board in list_of_boards:
    if board not in winning_boards:
        losing_board = board
        break

# play losing board until bingo to draw the right number of numbers
bingo = False
for i in range(5,len(drawn_nos)):
    if bingo:
        break
    already_drawn = drawn_nos[0:i]
    print(already_drawn)
    for row in losing_board:
        if set(row).issubset(already_drawn):
            print(row)
            print('bingo!')
            bingo = True

print("losing_board")
print(losing_board)
original_last_board = losing_board[0:5]
print("original_last_board")
print(original_last_board)

last_drawn = already_drawn[-1]
print(last_drawn)
print(already_drawn)

tot = 0
for i in original_last_board:
    for j in i:
        if j not in already_drawn:
            #print(f'keep: {j}')
            tot += j
        #else:
            #print(f'yeet: {j}')

print(tot)
final = tot * last_drawn
print(final)
