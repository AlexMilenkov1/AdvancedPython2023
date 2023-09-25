n = int(input())

matrix = []

for row in range(n):
    characters = list(input())

    matrix.append(characters)

searched_char = input()

position = None

for row in range(n):
    for col in range(n):
        if matrix[row][col] == searched_char:
            position = (row, col)
            print(position)
            exit()

if not position:
    print(f'{searched_char} does not occur in the matrix')
