from math import floor
from collections import deque

expression = input().split()

operators = {'*': lambda a, b: a * b,
             '+': lambda a, b: a + b,
             '-': lambda a, b: a - b,
             '/': lambda a, b: floor(a / b)}

numbers = deque()

for char in expression:
    if char in operators.keys():
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            numbers.appendleft(operators[char](first_num, second_num))

    else:
        numbers.append(int(char))

print(numbers[0])