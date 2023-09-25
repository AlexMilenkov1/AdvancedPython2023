data = input().split(', ')
rows, cols = int(data[0]), int(data[1])

matrix = []

for row in range(rows):
    numbers = [int(x) for x in input().split(', ')]

    matrix.append(numbers)

biggest_sum = 2.2250738585072014e-308
sub_matrix = None

for row in range(rows - 1):
    for col in range(cols - 1):
        current_number = matrix[row][col]
        next_to_number = matrix[row][col + 1]
        below_number = matrix[row + 1][col]
        diagonal_number = matrix[row + 1][col + 1]

        sum_numbers = current_number + next_to_number + below_number + diagonal_number

        if sum_numbers > biggest_sum:
            biggest_sum = sum_numbers
            sub_matrix = [[current_number, next_to_number], [below_number, diagonal_number]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(biggest_sum)
