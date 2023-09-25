rows, cols = input().split(', ')

matrix = []

result_of_sum = 0

for row in range(int(rows)):
    elements = [int(x) for x in input().split(', ')]
    result_of_sum += sum(elements)
    matrix.append(elements)

print(result_of_sum)
print(matrix)
