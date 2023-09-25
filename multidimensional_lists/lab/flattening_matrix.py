rows = int(input())

matrix = []

for row in range(rows):
    numbers = [int(x) for x in input().split(', ')]

    matrix.append(numbers)

flattened = []

for row_index in range(rows):
    for col_index in range(len(matrix[row_index])):
        flattened.append(matrix[row_index][col_index])

print(flattened)
