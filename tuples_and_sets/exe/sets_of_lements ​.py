n, m = input().split()

set_a = set()
set_b = set()

for _ in range(int(n)):
    number = int(input())

    set_a.add(number)

for _ in range(int(m)):
    number = int(input())

    set_b.add(number)

intersection = set_a.intersection(set_b)

print(*intersection, sep='\n')
