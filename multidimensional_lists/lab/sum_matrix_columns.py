rows, cols = input().split(', ')

matrix = []

for row in range(int(rows)):
    numbers = [int(x) for x in input().split()]

    matrix.append(numbers)

for col_index in range(int(cols)):
    sums = 0
    for row_index in range(int(rows)):
        sums += matrix[row_index][col_index]

    print(sums)
