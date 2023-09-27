def check_space(r, c, size):
    return 0 <= r < size and 0 <= c < size


def check_bomb(r, c):
    return f'{r},{c}' in bombs


rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

bombs = input().split()

for bomb in bombs:
    data = bomb.split(',')
    first_cord = int(data[0])
    second_cord = int(data[1])

    current_bomb = matrix[first_cord][second_cord]


    if check_space(first_cord - 1, second_cord, rows):
        top = matrix[first_cord - 1][second_cord]

        if top > 0 and not check_bomb(first_cord - 1, second_cord):
            matrix[first_cord - 1][second_cord] -= current_bomb

    if check_space(first_cord + 1, second_cord, rows):
        bottom = matrix[first_cord + 1][second_cord]

        if bottom > 0 and not check_bomb(first_cord + 1, second_cord):
            matrix[first_cord + 1][second_cord] -= current_bomb

    if check_space(first_cord, second_cord - 1, rows):
        left = matrix[first_cord][second_cord - 1]

        if left > 0 and not check_bomb(first_cord, second_cord - 1):
            matrix[first_cord][second_cord - 1] -= current_bomb

    if check_space(first_cord, second_cord + 1, rows):
        right = matrix[first_cord][second_cord + 1]

        if right > 0 and not check_bomb(first_cord, second_cord + 1):
            matrix[first_cord][second_cord + 1] -= current_bomb

    # diagonals

    if check_space(first_cord - 1, second_cord - 1, rows):
        top_left_diagonal = matrix[first_cord - 1][second_cord - 1]

        if top_left_diagonal > 0 and not check_bomb(first_cord - 1, second_cord - 1):
            matrix[first_cord - 1][second_cord - 1] -= current_bomb

    if check_space(first_cord - 1, second_cord + 1, rows):
        top_right_diagonal = matrix[first_cord - 1][second_cord + 1]

        if top_right_diagonal > 0 and not check_bomb(first_cord - 1, second_cord + 1):
            matrix[first_cord - 1][second_cord + 1] -= current_bomb

    if check_space(first_cord + 1, second_cord - 1, rows):
        bottom_left_diagonal = matrix[first_cord + 1][second_cord - 1]

        if bottom_left_diagonal > 0 and not check_bomb(first_cord + 1, second_cord - 1):
            matrix[first_cord + 1][second_cord - 1] -= current_bomb

    if check_space(first_cord + 1, second_cord + 1, rows):
        bottom_right_diagonal = matrix[first_cord + 1][second_cord + 1]

        if bottom_right_diagonal > 0 and not check_bomb(first_cord + 1, second_cord + 1):
            matrix[first_cord + 1][second_cord + 1] -= current_bomb

    matrix[first_cord][second_cord] = 0

alive_cells_count = 0
alive_cells_sum = 0

for r in range(rows):
    for c in range(rows):
        if matrix[r][c] > 0:
            alive_cells_count += 1

            alive_cells_sum += matrix[r][c]

print(f'Alive cells: {alive_cells_count}')
print(f'Sum: {alive_cells_sum}')
for r in range(rows):
    print(*matrix[r])
