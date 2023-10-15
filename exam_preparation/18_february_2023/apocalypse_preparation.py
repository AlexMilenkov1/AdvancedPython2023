from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

healing_items = {'Patch': 0, 'Bandage': 0, 'MedKit': 0}

while textiles and medicaments:
    first_value = textiles.popleft()
    second_value = medicaments.pop()

    values_sum = first_value + second_value

    if values_sum == 30:
        healing_items['Patch'] += 1
    elif values_sum == 40:
        healing_items['Bandage'] += 1
    elif values_sum == 100:
        healing_items['MedKit'] += 1
    elif values_sum > 100:
        healing_items['MedKit'] += 1
        remaining_value = values_sum - 100
        medicaments[-1] += remaining_value
    else:
        second_value += 10
        medicaments.append(second_value)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for item, count in sorted(healing_items.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    if count > 0:
        print(f'{item} - {count}')
if medicaments:
    print(f"Medicaments left: {', '.join(str(a) for a in reversed(medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(str(a) for a in textiles)}")
