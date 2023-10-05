def math_operations(*args, **kwargs):
    count = 0

    for el in args:
        count += 1

        if count == 1:
            kwargs['a'] += el
        elif count == 2:
            kwargs['s'] -= el
        elif count == 3:
            if el != 0:
                kwargs['d'] /= el
        elif count == 4:
            kwargs['m'] *= el
            count = 0

    sorted_numbers = dict(sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0])))

    result = []

    for key, value in sorted_numbers.items():
        result.append(f"{key}: {value:.1f}")

    return '\n'.join(result)


print(math_operations(6.0, a=0, s=0, d=5, m=0))