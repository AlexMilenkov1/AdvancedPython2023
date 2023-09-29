matrix = []
targets = 0
starting_position = []
shot_targets = []

for row in range(5):
    matrix.append(list(input().split()))
    for col in range(5):
        if matrix[row][col] == 'A':
            starting_position = [row, col]
        elif matrix[row][col] == 'x':
            targets += 1

n = int(input())

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for _ in range(n):
    command = input().split()

    if command[0] == 'shoot':
        direction = command[1]
        r = starting_position[0] + directions[direction][0]
        c = starting_position[1] + directions[direction][1]

        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == 'x':
                targets -= 1
                shot_targets.append([r, c])
                matrix[r][c] = '.'
                break
            r += directions[direction][0]
            c += directions[direction][1]
        if targets == 0:
            print(f"Training completed! All {len(shot_targets)} targets hit.")
            for el in shot_targets:
                print(el)
            break
    elif command[1] == 'move':
        direction = command[1]
        steps = int(command[2])

        r = starting_position[0]
        c = starting_position[1]

        if direction == 'up':
            r -= steps
        elif direction == 'down':
            r += steps
        elif direction == 'left':
            c -= steps
        elif direction == 'right':
            c += steps

        if 0 <= r < 5 and 0 <= c < 5 and matrix[r][c] == '.':
            matrix[r][c] = 'A'
            matrix[starting_position[0]][starting_position[1]] = '.'
            starting_position = [r, c]
else:
    print(f'Training not completed! {targets} targets left.')
    for el in shot_targets:
        print(el)
