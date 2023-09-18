clothes_in_box = [int(x) for x in input().split()]
capacity_of_rack = int(input())


rack_count = 0


while clothes_in_box:
    rack_count += 1

    current_rack_capacity = capacity_of_rack

    while clothes_in_box and clothes_in_box[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes_in_box.pop()

print(rack_count)

