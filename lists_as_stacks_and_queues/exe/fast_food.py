from collections import deque

quantity_of_food = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    if quantity_of_food >= orders[0] and len(orders) != 0:
        quantity_of_food = quantity_of_food - orders[0]

        orders.popleft()

    else:
        break

result = [str(x) for x in orders]

if len(orders) == 0:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join(result)}')