n = int(input())
racing_number = input()

matrix = []

car_pos = [0, 0]
first_tunnel = []
second_tunnel = []
passed_km = 0

for row in range(n):
    line = input().split()
    matrix.append(line)
    for col in range(n):
        if matrix[row][col] == 'T':
            if first_tunnel:
                second_tunnel = [row, col]
            else:
                first_tunnel = [row, col]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}


while True:
    direction = input()

    if direction == 'End':
        matrix[car_pos[0]][car_pos[1]] = 'C'
        print(f"Racing car {racing_number} DNF.")
        break

    new_row = directions[direction][0] + car_pos[0]
    new_col = directions[direction][1] + car_pos[1]

    if matrix[new_row][new_col] == '.':
        car_pos = [new_row, new_col]
        passed_km += 10
    elif matrix[new_row][new_col] == 'T':
        if new_row == first_tunnel[0] and new_col == first_tunnel[1]:
            car_pos = [second_tunnel[0], second_tunnel[1]]
            matrix[new_row][new_col] = '.'
            matrix[second_tunnel[0]][second_tunnel[1]] = '.'
            passed_km += 30
        elif new_row == second_tunnel[0] and new_col == second_tunnel[1]:
            car_pos = [first_tunnel[0], first_tunnel[1]]
            matrix[new_row][new_col] = '.'
            matrix[first_tunnel[0]][first_tunnel[1]] = '.'
            passed_km += 30
    elif matrix[new_row][new_col] == 'F':
        passed_km += 10
        matrix[new_row][new_col] = 'C'
        print(f"Racing car {racing_number} finished the stage!")
        break

print(f'Distance covered {passed_km} km.')
for row in range(n):
    print(''.join(matrix[row]))
