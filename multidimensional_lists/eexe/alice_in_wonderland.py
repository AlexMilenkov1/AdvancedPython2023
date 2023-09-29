n = int(input())

alice_position = []
matrix = []

for row in range(n):
    line = list(input().split())

    matrix.append(line)
    for col in range(n):
        item = matrix[row][col]

        if item == 'A':
            alice_position = [row, col]

bags_of_tea = 0
rabbit_hole_or_outside = False

alice_row = alice_position[0]
alice_col = alice_position[1]

matrix[alice_row][alice_col] = '*'

while bags_of_tea < 10:
    direction = input()

    if direction == 'up':
        alice_row -= 1

        if 0 <= alice_row < n and matrix[alice_row][alice_col] != 'R':
            tea = matrix[alice_row][alice_col]

            if tea.isdigit():
                bags_of_tea += int(tea)
            matrix[alice_row][alice_col] = '*'

        else:
            rabbit_hole_or_outside = True
            if 0 <= alice_row < n:
                matrix[alice_row][alice_col] = '*'
            break

    elif direction == 'down':
        alice_row += 1

        if 0 <= alice_row < n and matrix[alice_row][alice_col] != 'R':
            tea = matrix[alice_row][alice_col]

            if tea.isdigit():
                bags_of_tea += int(tea)
            matrix[alice_row][alice_col] = '*'

        else:
            rabbit_hole_or_outside = True
            if 0 <= alice_row < n:
                matrix[alice_row][alice_col] = '*'
            break

    elif direction == 'left':
        alice_col -= 1

        if 0 <= alice_col < n and matrix[alice_row][alice_col] != 'R':
            tea = matrix[alice_row][alice_col]

            if tea.isdigit():
                bags_of_tea += int(tea)
            matrix[alice_row][alice_col] = '*'

        else:
            rabbit_hole_or_outside = True
            if 0 <= alice_col < n:
                matrix[alice_row][alice_col] = '*'
            break

    elif direction == 'right':
        alice_col += 1

        if 0 <= alice_col < n and matrix[alice_row][alice_col] != 'R':
            tea = matrix[alice_row][alice_col]

            if tea.isdigit():
                bags_of_tea += int(tea)
            matrix[alice_row][alice_col] = '*'

        else:
            rabbit_hole_or_outside = True
            if 0 <= alice_col < n:
                matrix[alice_row][alice_col] = '*'
            break

if rabbit_hole_or_outside:
    print(f"Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
for row in range(n):
    print(*matrix[row])
