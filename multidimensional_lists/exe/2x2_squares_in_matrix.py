data = input().split()
rows = int(data[0])
cols = int(data[1])

squares_found = 0

matrix = [input().split() for _ in range(rows)]

for i in range(rows - 1):
    for j in range(cols - 1):
        current_character = matrix[i][j]
        next_to_character = matrix[i][j + 1]
        below_character = matrix[i + 1][j]
        diagonal_character = matrix[i + 1][j + 1]

        if next_to_character == current_character:
            if below_character == current_character:
                if diagonal_character == current_character:
                    squares_found += 1

print(squares_found)
