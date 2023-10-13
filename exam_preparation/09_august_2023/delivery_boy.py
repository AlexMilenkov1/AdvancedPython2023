data = input().split()
rows = int(data[0])
cols = int(data[1])

matrix = []

boy_position = []
starting_pos = []

for row in range(rows):
    line = list(input())
    matrix.append(line)
    for col in range(cols):
        if matrix[row][col] == 'B':
            boy_position = [row, col]
            starting_pos = [row, col]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}


while True:
    direction = input()

    updated_row = directions[direction][0] + boy_position[0]
    updated_col = directions[direction][1] + boy_position[1]

    if 0 <= updated_row < rows and 0 <= updated_col < cols:
        if matrix[updated_row][updated_col] == 'P':
            matrix[updated_row][updated_col] = 'R'
            print("Pizza is collected. 10 minutes for delivery.")
            boy_position = [updated_row, updated_col]
        elif matrix[updated_row][updated_col] == 'A':
            matrix[updated_row][updated_col] = 'P'
            print("Pizza is delivered on time! Next order...")
            break
        elif matrix[updated_row][updated_col] == '-':
            matrix[updated_row][updated_col] = '.'
            boy_position = [updated_row, updated_col]
        elif matrix[updated_row][updated_col] == '*':
            continue

    else:
        print("The delivery is late. Order is canceled.")
        matrix[starting_pos[0]][starting_pos[1]] = ' '
        break

for row in range(rows):
    print(''.join(matrix[row]))
