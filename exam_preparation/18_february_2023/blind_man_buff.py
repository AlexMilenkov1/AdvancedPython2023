data = input().split()
rows = int(data[0])
cols = int(data[1])

player_position = []
touched_opponents = 0
moves_made = 0

playing_field = []

for row in range(rows):
    line = list(input().split())
    playing_field.append(line)
    for col in range(cols):
        if playing_field[row][col] == 'B':
            player_position = [row, col]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    direction = input()

    if direction == 'Finish':
        break

    if touched_opponents == 3:
        break

    updated_row = directions[direction][0] + player_position[0]
    updated_col = directions[direction][1] + player_position[1]

    if 0 <= updated_row < rows and 0 <= updated_col < cols:
        new_position = playing_field[updated_row][updated_col]
        if new_position == 'O':
            continue
        if new_position == 'P':
            touched_opponents += 1
            player_position = [updated_row, updated_col]
            new_position = '-'
            moves_made += 1
        elif new_position == '-':
            moves_made += 1
            player_position = [updated_row, updated_col]
        elif new_position == 'B':
            moves_made += 1
            player_position = [updated_row, updated_col]

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")
