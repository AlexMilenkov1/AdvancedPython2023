from collections import deque

programmers_time = deque(int(x) for x in input().split())
number_of_tasks = deque(int(x) for x in input().split())

duckies_storage = {'Darth Vader Ducky': 0, 'Thor Ducky': 0, 'Big Blue Rubber Ducky': 0, 'Small Yellow Rubber Ducky': 0}

while programmers_time and number_of_tasks:
    first_value = programmers_time.popleft()
    last_value = number_of_tasks.pop()

    multiplied_values = first_value * last_value

    if multiplied_values in range(0, 61):
        duckies_storage['Darth Vader Ducky'] += 1
    elif multiplied_values in range(61, 121):
        duckies_storage['Thor Ducky'] += 1
    elif multiplied_values in range(121, 181):
        duckies_storage['Big Blue Rubber Ducky'] += 1
    elif multiplied_values in range(181, 241):
        duckies_storage['Small Yellow Rubber Ducky'] += 1
    elif multiplied_values > 240:
        last_value -= 2
        programmers_time.append(first_value)
        number_of_tasks.append(last_value)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck, count in duckies_storage.items():
    print(f'{duck}: {count}')
