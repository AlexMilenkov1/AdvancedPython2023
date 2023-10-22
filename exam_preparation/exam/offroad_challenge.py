from collections import deque

initial_fuel = deque(int(x) for x in input().split())
additional_consumption_index = deque(int(x) for x in input().split())
amount_of_fuel_needed = deque(int(x) for x in input().split())

reached_altitude = []

current_altitude = 0

while initial_fuel and additional_consumption_index:
    last_fuel_quantity = initial_fuel.pop()
    first_index = additional_consumption_index.popleft()

    subtracted_values = last_fuel_quantity - first_index

    if subtracted_values >= amount_of_fuel_needed[0]:
        amount_of_fuel_needed.popleft()
        current_altitude += 1
        reached_altitude.append(f'Altitude {current_altitude}')
        print(f'John has reached: Altitude {current_altitude}')
    else:
        current_altitude += 1
        print(f"John did not reach: Altitude {current_altitude}")
        break

if not amount_of_fuel_needed:
    print("John has reached all the altitudes and managed to reach the top!")
elif amount_of_fuel_needed and reached_altitude:
    print("John failed to reach the top.")
    print(f'Reached altitudes: {", ".join(reached_altitude)}')
elif amount_of_fuel_needed and not reached_altitude:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
