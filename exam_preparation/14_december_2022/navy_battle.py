n = int(input())

battlefield = []

submarine_coordinates = []
starting_coordinates = []

battle_cruises = 0
hit_mines = 3

for row in range(n):
    line = list(input())
    battlefield.append(line)
    for col in range(n):
        if battlefield[row][col] == 'S':
            submarine_coordinates = [row, col]
            starting_coordinates = [row, col]


directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    direction = input()

    new_row = directions[direction][0] + submarine_coordinates[0]
    new_col = directions[direction][1] + submarine_coordinates[1]

    new_pos = battlefield[new_row][new_col]

    if new_pos == '-':
        submarine_coordinates = [new_row, new_col]
    elif new_pos == '*':
        battlefield[new_row][new_col] = '-'
        submarine_coordinates = [new_row, new_col]
        hit_mines -= 1

        if hit_mines == 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_coordinates[0]}, {submarine_coordinates[1]}]!")
            battlefield[starting_coordinates[0]][starting_coordinates[1]] = '-'
            battlefield[new_row][new_col] = 'S'
            break
    elif new_pos == 'C':
        battle_cruises += 1
        submarine_coordinates = [new_row, new_col]
        battlefield[new_row][new_col] = '-'

        if battle_cruises == 3:
            print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
            battlefield[starting_coordinates[0]][starting_coordinates[1]] = '-'
            battlefield[new_row][new_col] = 'S'
            break
    elif new_pos == 'S':
        submarine_coordinates = [new_row, new_col]

for row in range(n):
    print(''.join(battlefield[row]))
