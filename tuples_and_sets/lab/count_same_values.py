numbers = [float(x) for x in input().split()]

occurrences = {}

for number in numbers:
    if number not in occurrences:
        occurrences[str(number)] = []

    occurrences[str(number)].append(numbers.count(number))

for key, value in occurrences.items():
    print(f'{key} - {value[0]} times')
