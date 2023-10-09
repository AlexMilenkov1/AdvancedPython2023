file = open('numbers.txt', 'r')

total_sum = 0

for line in file:
    total_sum += int(line)

print(total_sum)

file.close()

print(file.closed)

with open("file.txt", "w") as f:
    f.write("Hello World!!!")

print(f.closed)