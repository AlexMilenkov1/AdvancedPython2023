n = int(input())

board = []
knights = []

for row in range(n):
    line = [x for x in input()]

    board.append(line)
    for col in range(n):
        if board[row][col] == 'K':
            knights.append([row, col])

possible_moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

removed_knights = 0

while True:
    max_hits = 0
    max_knight = [0, 0]

    for k_row, k_col in knights:
        current_hits = 0
        for move in possible_moves:
            new_position_row = k_row + move[0]
            new_position_col = k_col + move[1]

            if 0 <= new_position_row < n and 0 <= new_position_col < n:
                if board[new_position_row][new_position_col] == 'K':
                    current_hits += 1

        if current_hits > max_hits:
            max_knight = [k_row, k_col]
            max_hits = current_hits

    if max_hits == 0:
        break

    removed_knights += 1
    knights.remove(max_knight)
    board[max_knight[0]][max_knight[1]] = '0'

print(removed_knights)
