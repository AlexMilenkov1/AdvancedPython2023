n = int(input())

parking = set()

for _ in range(n):
    car_info = input().split(', ')

    if car_info[0] == 'IN':
        parking.add(car_info[1])

    else:
        if car_info[1] in parking:
            parking.remove(car_info[1])

if parking:
    for car in parking:
        print(car)
else:
    print('Parking Lot is Empty')
