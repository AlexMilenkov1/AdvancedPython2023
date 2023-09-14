expression = input()

opening_brackets = []

for index in range(len(expression)):
    if expression[index] == '(':
        opening_brackets.append(index)
    elif expression[index] == ')':
        start_index = opening_brackets.pop()
        end_index = index + 1

        new_expression = expression[start_index:end_index]

        print(new_expression)