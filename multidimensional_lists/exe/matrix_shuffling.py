data = input().split()
rows = int(data[0])
cols = int(data[1])

matrix = [input().split() for _ in range(rows)]

while True:
    command = input().split()

    is_valid = False

    if command[0] == 'END':
        break

    if len(command) == 5:

        word = command[0]
        row_1 = int(command[1])
        col_1 = int(command[2])
        row_2 = int(command[3])
        col_2 = int(command[4])

        if word == 'swap' and row_1 >= 0 and row_2 >= 0 and col_1 >= 0 and col_2 >= 0:
            if rows >= row_1 and rows >= row_2:
                if cols >= col_1 and cols >= col_2:
                    matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2],  matrix[row_1][col_1]

                    is_valid = True

    if is_valid:
        for row in range(rows):
            print(*matrix[row])
    else:
        print('Invalid input!')
