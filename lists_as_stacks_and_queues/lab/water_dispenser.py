from collections import deque

quantity_of_water = int(input())

people_waiting = deque([])

while True:
    name = input()

    if name == 'Start':
        break

    people_waiting.append(name)

while True:
    command = input().split()

    if command[0] == 'End':
        break

    if len(command) == 1:
        liters = int(command[0])

        if quantity_of_water >= liters:
            print(f"{people_waiting.popleft()} got water")
            quantity_of_water -= liters
        else:
            print(f"{people_waiting.popleft()} must wait")

    else:
        liters_to_fill = int(command[1])

        quantity_of_water += liters_to_fill

print(f"{quantity_of_water} liters left")
