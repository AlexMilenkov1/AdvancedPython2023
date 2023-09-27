def have_space(r, c, size):
    return 0 <= r < size and 0 <= c < size


field_size = int(input())
commands = input().split()

matrix = []

coal_to_collect = 0
is_over = False
starting_pos = [0, 0]

for row in range(field_size):
    line = input().split()

    matrix.append(line)

    for index in range(len(line)):
        if line[index] == 'c':
            coal_to_collect += 1

        elif line[index] == 's':
            starting_pos[0] = row
            starting_pos[1] = index

for command in commands:
    if command == 'up':
        if have_space(starting_pos[0] - 1, starting_pos[1], field_size):
            starting_pos[0] -= 1
    elif command == 'down':
        if have_space(starting_pos[0] + 1, starting_pos[1], field_size):
            starting_pos[0] += 1
    elif command == 'right':
        if have_space(starting_pos[0], starting_pos[1] + 1, field_size):
            starting_pos[1] += 1
    elif command == 'left':
        if have_space(starting_pos[0], starting_pos[1] - 1, field_size):
            starting_pos[1] -= 1

    if matrix[starting_pos[0]][starting_pos[1]] == 'e':
        is_over = True
        print(f"Game over! ({starting_pos[0]}, {starting_pos[1]})")
        break

    if matrix[starting_pos[0]][starting_pos[1]] == 'c':
        coal_to_collect -= 1

        matrix[starting_pos[0]][starting_pos[1]] = '*'

        if coal_to_collect == 0:
            is_over = True
            print(f"You collected all coal! ({starting_pos[0]}, {starting_pos[1]})")
            break

if not is_over:
    print(f"{coal_to_collect} pieces of coal left. ({starting_pos[0]}, {starting_pos[1]})")
