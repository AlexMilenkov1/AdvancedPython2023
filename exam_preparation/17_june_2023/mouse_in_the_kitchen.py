data = input().split(',')
rows = int(data[0])
cols = int(data[1])

pieces_of_cheese = 0
mouse_pos = []

matrix = []

for row in range(rows):
    line = list(x for x in input())
    matrix.append(line)

    for col in range(cols):
        if matrix[row][col] == 'M':
            mouse_pos = [row, col]
        if matrix[row][col] == 'C':
            pieces_of_cheese += 1

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while pieces_of_cheese > 0:
    direction = input()

    if direction == 'danger' and pieces_of_cheese > 0:
        print("Mouse will come back later!")
        break

    new_row = directions[direction][0] + mouse_pos[0]
    new_col = directions[direction][1] + mouse_pos[1]

    if 0 <= new_row < rows and 0 <= new_col < cols:
        matrix[mouse_pos[0]][mouse_pos[1]] = '*'

        if matrix[new_row][new_col] == 'C':
            pieces_of_cheese -= 1
            matrix[new_row][new_col] = '*'
            mouse_pos = [new_row, new_col]

        elif matrix[new_row][new_col] == 'T':
            print("Mouse is trapped!")
            matrix[mouse_pos[0]][mouse_pos[1]] = '*'
            matrix[new_row][new_col] = 'M'
            mouse_pos = [new_row, new_col]
            break

        elif matrix[new_row][new_col] == '@':
            continue

        elif matrix[new_row][new_col] == '*':
            mouse_pos = [new_row, new_col]
            matrix[new_row][new_col] = 'M'

    else:
        print("No more cheese for tonight!")
        break

if pieces_of_cheese == 0:
    matrix[mouse_pos[0]][mouse_pos[1]] = 'M'
    print("Happy mouse! All the cheese is eaten, good night!")
for r in range(rows):
    print(''.join(matrix[r]))
