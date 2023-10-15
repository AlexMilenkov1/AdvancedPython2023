n = int(input())
input_directions = input().split(', ')

squirrel_position = []
collected_hazelnuts = 0
matrix = []

for row in range(n):
    line = list(input())
    matrix.append(line)
    for col in range(n):
        if matrix[row][col] == 's':
            squirrel_position = [row, col]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

is_trapped = False
out_of_field = False

for direction in input_directions:
    new_row = directions[direction][0] + squirrel_position[0]
    new_col = directions[direction][1] + squirrel_position[1]

    if 0 <= new_row < n and 0 <= new_col < n:
        if matrix[new_row][new_col] == 'h':
            collected_hazelnuts += 1
            matrix[new_row][new_col] = '*'
            squirrel_position = [new_row, new_col]
            if collected_hazelnuts == 3:
                break
        elif matrix[new_row][new_col] == '*':
            squirrel_position = [new_row, new_col]
        elif matrix[new_row][new_col] == 't':
            is_trapped = True
            break
        elif matrix[new_row][new_col] == 's':
            squirrel_position = [new_row, new_col]
    else:
        out_of_field = True
        break

if is_trapped:
    print("Unfortunately, the squirrel stepped on a trap...")
elif out_of_field:
    print("The squirrel is out of the field.")
else:
    if collected_hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
    elif collected_hazelnuts < 3:
        print("There are more hazelnuts to collect.")
print(f'Hazelnuts collected: {collected_hazelnuts}')
