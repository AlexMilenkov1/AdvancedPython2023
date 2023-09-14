from collections import deque

players = deque(input().split())
rotations = int(input()) - 1

while len(players) > 1:
    players.rotate(-rotations)

    print(f"Removed {players.popleft()}")

print(f'Last is {players.pop()}')
