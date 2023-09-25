first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    full_command = input().split()

    command = full_command[0] + " " + full_command[1]
    numbers = set(int(x) for x in full_command[2:])

    if command == 'Add First':
        first_sequence.update(numbers)
    elif command == 'Add Second':
        second_sequence.update(numbers)
    elif command == 'Remove First':
        first_sequence.difference_update(numbers)
    elif command == 'Remove Second':
        second_sequence.difference_update(numbers)
    else:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')