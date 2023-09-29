n = int(input())

bunny_position = []

matrix = []

for row in range(n):
    line = list(input().split())

    matrix.append(line)
    for col in range(n):
        element = matrix[row][col]

        if element == 'B':
            bunny_position = [row, col]

best_direction = None
best_field_positions = []
total_number_eggs = 0

possible_directions = ['up', 'down', 'left', 'right']

for direction in possible_directions:
    current_total_eggs = 0
    current_field_pos = []

    if direction == 'up':
        bunny_row = bunny_position[0]
        bunny_col = bunny_position[1]

        while True:
            bunny_row -= 1

            if 0 <= bunny_row < n:
                if matrix[bunny_row][bunny_col] == 'X':
                    break

                current_total_eggs += int(matrix[bunny_row][bunny_col])
                current_field_pos.append([bunny_row, bunny_col])
            else:
                break

    elif direction == 'down':
        bunny_row = bunny_position[0]
        bunny_col = bunny_position[1]

        while True:
            bunny_row += 1

            if 0 <= bunny_row < n:
                if matrix[bunny_row][bunny_col] == 'X':
                    break

                current_total_eggs += int(matrix[bunny_row][bunny_col])
                current_field_pos.append([bunny_row, bunny_col])
            else:
                break

    elif direction == 'left':
        bunny_row = bunny_position[0]
        bunny_col = bunny_position[1]

        while True:
            bunny_col -= 1

            if 0 <= bunny_col < n:
                if matrix[bunny_row][bunny_col] == 'X':
                    break

                current_total_eggs += int(matrix[bunny_row][bunny_col])
                current_field_pos.append([bunny_row, bunny_col])
            else:
                break

    elif direction == 'right':
        bunny_row = bunny_position[0]
        bunny_col = bunny_position[1]

        while True:
            bunny_col += 1

            if 0 <= bunny_col < n:
                if matrix[bunny_row][bunny_col] == 'X':
                    break

                current_total_eggs += int(matrix[bunny_row][bunny_col])
                current_field_pos.append([bunny_row, bunny_col])
            else:
                break

    if current_total_eggs >= total_number_eggs:
        best_field_positions = current_field_pos
        best_direction = direction
        total_number_eggs = current_total_eggs

print(best_direction)
for pos in best_field_positions:
    print(pos)
print(total_number_eggs)
