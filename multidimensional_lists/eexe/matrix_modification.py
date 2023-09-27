rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    commands = input().split()

    if commands[0] == 'END':
        break

    name_of_command = commands[0]
    row = int(commands[1])
    col = int(commands[2])
    value = int(commands[3])

    if name_of_command == 'Add':
        if 0 <= row < len(matrix[0]) and 0 <= col < len(matrix[0]):
            matrix[row][col] += value
        else:
            print('Invalid coordinates')
    else:
        if 0 <= row < len(matrix[0]) and 0 <= col < len(matrix[0]):
            matrix[row][col] -= value
        else:
            print('Invalid coordinates')

for row in range(rows):
    print(*matrix[row])
