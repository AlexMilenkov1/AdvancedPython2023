n = int(input())

matrix = []

for rows in range(n):
    numbers = [int(x) for x in input().split()]

    matrix.append(numbers)

sums = 0

for rows_index in range(n):
    sums += matrix[rows_index][rows_index]

print(sums)
