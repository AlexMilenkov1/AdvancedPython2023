rows = int(input())

matrix = []

for row in range(rows):
    numbers = [int(x) for x in input().split(', ') if int(x) % 2 == 0]

    matrix.append(numbers)

print(matrix)
