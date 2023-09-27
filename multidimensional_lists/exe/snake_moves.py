from collections import deque

data = input().split()
rows = int(data[0])
cols = int(data[1])

text = deque(input())

matrix = []

for row in range(rows):
    matrix.append([''] * cols)
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = text[0]
        else:
            matrix[row][-1 - col] = text[0]
        text.rotate(-1)

for r in range(rows):
    print(''.join(matrix[r]))