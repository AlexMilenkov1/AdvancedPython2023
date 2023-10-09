numbers_dictionary = {}

while True:
    string_number = input()
    if string_number == 'Search':
        break
    number = input()
    if number.isdigit():
        numbers_dictionary[string_number] = int(number)
    else:
        print("The variable number must be an integer")


while True:
    searched_num_text = input()
    if searched_num_text == 'Remove':
        break
    print(numbers_dictionary[searched_num_text])


while True:
    line = input()
    if line == 'End':
        break
    if line in numbers_dictionary.keys():
        del numbers_dictionary[line]
    else:
        print("Number does not exist in dictionary")

print(numbers_dictionary)
