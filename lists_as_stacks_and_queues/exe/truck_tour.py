from collections import deque

n = int(input())

start_position = 0
stops = 0

petrol_pumps = deque()

for _ in range(n):
    fuel, distance = input().split()
    petrol_pumps.append([fuel, distance])

while stops < n:
    current_fuel = 0

    for index in range(n):
        current_fuel += int(petrol_pumps[index][0])
        distance = int(petrol_pumps[index][1])

        if current_fuel < distance:
            petrol_pumps.rotate(-1)

            stops = 0
            start_position += 1
            break

        current_fuel -= distance
        stops += 1

print(start_position)