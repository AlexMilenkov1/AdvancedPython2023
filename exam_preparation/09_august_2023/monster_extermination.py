from collections import deque

monsters_armor = deque(int(x) for x in input().split(','))
soldier_striking_impact = deque(int(x) for x in input().split(','))

total_monsters_killed = 0

while monsters_armor and soldier_striking_impact:
    first_armor_value = monsters_armor.popleft()
    last_striking_value = soldier_striking_impact.pop()

    if last_striking_value >= first_armor_value:
        total_monsters_killed += 1
        last_striking_value -= first_armor_value

        if soldier_striking_impact:
            soldier_striking_impact[-1] += last_striking_value
        elif not soldier_striking_impact and last_striking_value > 0:
            soldier_striking_impact.append(last_striking_value)
    else:
        first_armor_value -= last_striking_value
        monsters_armor.append(first_armor_value)

if not monsters_armor:
    print("All monsters have been killed!")
if not soldier_striking_impact:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {total_monsters_killed}")
