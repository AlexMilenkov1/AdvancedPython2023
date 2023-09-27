data = input().split()
rows = int(data[0])
cols = int(data[1])

start_char = ord('a')

for row in range(rows):
    for col in range(cols):
        print(f'{chr(start_char + row)}{chr(start_char + row + col)}{chr(start_char + row)}', end=' ')
    print()
