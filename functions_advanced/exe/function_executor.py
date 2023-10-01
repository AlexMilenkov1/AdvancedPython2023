def func_executor(*args):
    result = []

    for funct, data in args:
        result.append(f"{funct.__name__} - {funct(*data)}")
    return '\n'.join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
