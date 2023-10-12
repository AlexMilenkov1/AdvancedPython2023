with open('text.txt', 'r') as f:
    for row, line in enumerate(f.readlines()):
        if row % 2 == 0:
            for ch in line:
                if ch in ["-", ",", ".", "!", "?"]:
                    line = line.replace(ch, '@')
            print(''.join(reversed(line.split())))