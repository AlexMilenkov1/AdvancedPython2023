text = input()

ordered_set = sorted(set(text))

for char in ordered_set:
    print(f'{char}: {text.count(char)} time/s')
