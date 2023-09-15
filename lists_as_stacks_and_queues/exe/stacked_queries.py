number_of_lines = int(input())

stack = []

for line in range(number_of_lines):
    query = input().split()

    if len(query) == 2:
        number = int(query[1])

        stack.append(number)
    else:
        command_number = int(query[0])
        if len(stack) > 0:
            if command_number == 2:
                    stack.pop()
            elif command_number == 3:
                print(max(stack))
            elif command_number == 4:
                print(min(stack))

while len(stack) > 1:
    print(stack.pop(), end=', ')

# Print the last element without a comma
if len(stack) == 1:
    print(stack.pop())
