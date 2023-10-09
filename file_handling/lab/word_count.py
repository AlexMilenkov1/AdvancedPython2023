result = {}
search = ''

with open('words.txt', 'r') as file_1:

    with open('input.txt', 'r') as file_2:
        for line in file_2:
            search += line

        for el in file_1:
            for word in el.split():
                result[word] = word.count(search)
print(search)
print(result)