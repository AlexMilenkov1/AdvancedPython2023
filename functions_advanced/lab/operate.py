from functools import reduce


def operate(operator, *args):
    def add():
        return reduce(lambda a, b: a + b, args)

    def subtract():
        return reduce(lambda a, b: a - b, args)

    def multiply():
        return reduce(lambda a, b: a * b, args)

    def divide():
        return reduce(lambda a, b: a / b, args)

    dict = {"+": add(), "-": subtract(), "/": divide(), "*": multiply()}

    return dict[operator]


print(operate("-", 1, 2, 3))
print(operate("/", 3, 4))
