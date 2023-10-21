n = 6

matrix = []

for row in range(n):
    line = input().split()
    matrix.append(line)

first_position = list(int(x) for x in input() if x.isdigit())

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    info = input().split(', ')

    if info[0] == 'Stop':
        break

    command = info[0]
    direction = info[1]

    updated_row = directions[direction][0] + first_position[0]
    updated_col = directions[direction][1] + first_position[1]

    if command == 'Create':
        value = info[2]
        if matrix[updated_row][updated_col] == '.':
            matrix[updated_row][updated_col] = value
            first_position = [updated_row, updated_col]
    elif command == 'Update':
        value = info[2]
        if matrix[updated_row][updated_col] != '.':
            matrix[updated_row][updated_col] = value
            first_position = [updated_row, updated_col]
    elif command == 'Delete':
        if matrix[updated_row][updated_col] != '.':
            matrix[updated_row][updated_col] = '.'
            first_position = [updated_row, updated_col]
    elif command == 'Read':
        if matrix[updated_row][updated_col] != '.':
            print(matrix[updated_row][updated_col])
            first_position = [updated_row, updated_col]

for row in range(n):
    print(' '.join(matrix[row]))
