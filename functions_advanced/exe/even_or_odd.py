def even_odd(*args):
    command = args[-1]

    even_nums = []
    odd_nums = []

    for index in range(len(args) - 1):
        if args[index] % 2 == 0:
            even_nums.append(args[index])
        else:
            odd_nums.append(args[index])

    if command == 'even':
        return even_nums
    return odd_nums


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))