n = int(input())

fishing_area = []
starting_position = []
passage_amount = 0
trapped = False

for row in range(n):
    line = list(input())
    fishing_area.append(line)
    for col in range(n):
        if fishing_area[row][col] == 'S':
            starting_position = [row, col]
            fishing_area[row][col] = '-'

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    direction = input()

    if direction == 'collect the nets':
        fishing_area[starting_position[0]][starting_position[1]] = 'S'
        break

    updated_row = directions[direction][0] + starting_position[0]
    updated_col = directions[direction][1] + starting_position[1]

    if not 0 <= updated_row < n:
        if direction == 'up':
            updated_row = n - 1
        elif direction == 'down':
            updated_row = 0
    elif not 0 <= updated_col < n:
        if direction == 'left':
            updated_col = n - 1
        elif direction == 'right':
            updated_col = 0

    if fishing_area[updated_row][updated_col].isdigit():
        passage_amount += int(fishing_area[updated_row][updated_col])
        fishing_area[updated_row][updated_col] = '-'
        starting_position = [updated_row, updated_col]
    elif fishing_area[updated_row][updated_col] == 'W':
        trapped = True
        starting_position = [updated_row, updated_col]
        break
    elif fishing_area[updated_row][updated_col] == '-':
        starting_position = [updated_row, updated_col]

if trapped:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{starting_position[0]},{starting_position[1]}]")
else:
    if passage_amount >= 20:
        print("Success! You managed to reach the quota!")
    elif passage_amount < 20:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - passage_amount} tons of fish more.")
    if passage_amount > 0:
        print(f"Amount of fish caught: {passage_amount} tons.")
    if not trapped:
        for row in range(n):
            print(''.join(fishing_area[row]))
