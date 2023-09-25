from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())

total_honey_made = 0

formula_for_honey = {"+": lambda bee, matched_nectar: abs(bee + matched_nectar),
                     "-": lambda bee, matched_nectar: abs(bee - matched_nectar),
                     "*": lambda bee, matched_nectar: abs(bee * matched_nectar),
                     "/": lambda bee, matched_nectar: abs(bee / matched_nectar)}

while bees and nectar:
    if bees[0] > nectar[-1]:
        nectar.pop()
    else:
        if symbols[0] == '/' and nectar[-1] == 0:
            bees.popleft()
            nectar.pop()
            symbols.popleft()
            continue

        total_honey_made += formula_for_honey[symbols[0]](bees[0], nectar[-1])
        bees.popleft()
        nectar.pop()
        symbols.popleft()

print(f'Total honey made: {total_honey_made}')
if bees:
    print(f'Bees left: {", ".join(str(x) for x in bees)}')
if nectar:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')
