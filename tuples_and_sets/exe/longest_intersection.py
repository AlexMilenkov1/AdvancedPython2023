n = int(input())

longest_intersection = set()

for _ in range(n):
    first_range, second_range = input().split('-')
    first_start, first_end = [int(x) for x in first_range.split(',')]
    second_start, second_end = [int(x) for x in second_range.split(',')]

    first_current_range = set(range(first_start, first_end + 1))
    second_current_range = set(range(second_start, second_end + 1))

    current_intersection = first_current_range & second_current_range

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')
