n = int(input())

odd_set = set()
even_set = set()

result = None

for count in range(1, n + 1):
    sum_numbers = sum([ord(x) for x in input()]) // count

    if sum_numbers % 2 == 0:
        even_set.add(sum_numbers)
    else:
        odd_set.add(sum_numbers)

if sum(odd_set) == sum(even_set):
    result = (odd_set.union(even_set))

elif sum(odd_set) > sum(even_set):
    result = (odd_set.difference(even_set))

else:
    result = (even_set.symmetric_difference(odd_set))

print(*result, sep=', ')
