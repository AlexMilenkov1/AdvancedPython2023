from string import punctuation

with open('text.txt') as f:
    result = []

    for row, line in enumerate(f.readlines()):
        letters_count = 0
        punctuations_count = 0

        for ch in line:
            if ch in punctuation:
                punctuations_count += 1
            elif ch.isalpha():
                letters_count += 1

        result.append(f'Line {row+1}: {line.strip()} ({letters_count})({punctuations_count})')

    with open('text.txt', 'w') as new_f:
        print('\n'.join(result))
