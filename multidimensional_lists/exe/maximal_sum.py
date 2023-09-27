data = input().split()
rows = int(data[0])
cols = int(data[1])

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

biggest_sum = float('-inf')

sub_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        current_number = matrix[row][col]

        current_matrix = []
        current_biggest_sum = 0

        for i in range(3):
                row_ = [matrix[row + i][col + j] for j in range(3)]

                current_matrix.append(row_)

                current_biggest_sum += sum(row_)

        if current_biggest_sum > biggest_sum:
            biggest_sum = current_biggest_sum

            sub_matrix = current_matrix

print(f'Sum = {biggest_sum}')
print(*sub_matrix[0])
print(*sub_matrix[1])
print(*sub_matrix[2])
