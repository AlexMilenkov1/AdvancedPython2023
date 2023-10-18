from collections import deque

milligrams_of_caffeine = deque(int(x) for x in input().split(', '))
energy_drinks = deque(int(x) for x in input().split(', '))

stamats_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    last_milligrams_of_caffeine = milligrams_of_caffeine.pop()
    first_energy_drink = energy_drinks.popleft()

    caffeine_intake = last_milligrams_of_caffeine * first_energy_drink

    if caffeine_intake + stamats_caffeine <= 300:
        stamats_caffeine += caffeine_intake
    else:
        energy_drinks.append(first_energy_drink)
        if stamats_caffeine >= 30:
            stamats_caffeine -= 30
        else:
            stamats_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamats_caffeine} mg caffeine.")
