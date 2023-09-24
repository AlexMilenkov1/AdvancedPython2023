from collections import deque

robots_data = deque(input().split(';'))
hours, minutes, seconds = [int(x) for x in input().split(':')]
starting_time_seconds = (hours * 3600) + (minutes * 60) + seconds

products = deque()
robots = []

for robot in robots_data:
    robot_name, processing_time = robot.split('-')
    time_busyness = 0
    robots.append({'name': robot_name, 'data': [int(processing_time), int(time_busyness)]})

while True:

    product = input()

    if product == 'End':
        break

    products.append(product)

while products:
    starting_time_seconds += 1
    current_product = products.popleft()
    is_taken = False

    for robot in robots:
        if robot['data'][1] <= starting_time_seconds:
            robot['data'][1] = starting_time_seconds + robot['data'][0]

            hours = starting_time_seconds // 3600
            minutes = (starting_time_seconds % 3600) // 60
            seconds = (starting_time_seconds % 3600) % 60
            hours %= 24

            print(f'{robot["name"]} - {current_product} [{hours:02d}:{minutes:02d}:{seconds:02d}]')

            is_taken = True
            break

    if not is_taken:
        products.append(current_product)
