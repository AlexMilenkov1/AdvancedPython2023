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

            else:
                if green_light_seconds > 0:
                    car_rest = queue_of_cars[0][:green_light_seconds]

                    if len(car_rest) <= free_window:
                        total_cars_passed += 1
                    else:
                        result = car_rest[:free_window]
                        print('A crash happened!')
                        print(f'{queue_of_cars[0]} was hit at {result[0]}.')

            if not queue_of_cars:
                green_light_seconds = copy

    queue_of_cars.append(car)
