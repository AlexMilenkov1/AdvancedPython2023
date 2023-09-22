from collections import deque

green_light_seconds = int(input())
copy = green_light_seconds
free_window = int(input())

queue_of_cars = deque()

total_cars_passed = 0

while True:
    car = input()

    if car == 'END':
        break

    if car == 'green':
        while queue_of_cars:
            if len(queue_of_cars[0]) <= green_light_seconds:
                green_light_seconds -= len(queue_of_cars[0])
                total_cars_passed += 1

                queue_of_cars.popleft()

            elif green_light_seconds > 0:
                free_window_attend = queue_of_cars[0][green_light_seconds:]

                green_light_seconds = 0

                if len(free_window_attend) <= free_window:
                    total_cars_passed += 1

                    queue_of_cars.popleft()

                else:
                    crash = free_window_attend[free_window:]

                    print('A crash happened!')
                    print(f'{queue_of_cars.popleft()} was hit at {crash[0]}.')

                    exit()
            else:
                queue_of_cars.clear()
                break

        if not queue_of_cars:
            green_light_seconds = copy
    else:
        queue_of_cars.append(car)

print('Everyone is safe.')
print(f'{total_cars_passed} total cars passed the crossroads.')
