from collections import deque

seats = input().split(', ')
first_sequence = deque(int(x) for x in input().split(', '))
second_sequence = deque(int(x) for x in input().split(', '))

rotation_count = 0
seat_matches = []

while rotation_count < 10 and len(seat_matches) != 3:
    first_number = first_sequence.popleft()
    last_number = second_sequence.pop()

    rotation_count += 1

    sum_values = first_number + last_number
    character = chr(sum_values)

    first_match = f'{first_number}{character}'
    second_match = f'{last_number}{character}'

    if first_match in seats:
        seats.remove(first_match)
        seat_matches.append(first_match)
    elif second_match in seats:
        seats.remove(second_match)
        seat_matches.append(second_match)
    else:
        first_sequence.append(first_number)
        second_sequence.appendleft(last_number)

print(f'Seat matches: {", ".join(seat_matches)}')
print(f'Rotations count: {rotation_count}')
