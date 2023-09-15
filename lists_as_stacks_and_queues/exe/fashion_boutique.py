clothes_in_box = [int(x) for x in input().split()]
capacity_of_rack = int(input())

copy = capacity_of_rack

rack_count = 0

while clothes_in_box:
    if capacity_of_rack > clothes_in_box[-1]:
        capacity_of_rack -= clothes_in_box[-1]

        clothes_in_box.pop()

    elif capacity_of_rack == clothes_in_box[-1]:
        rack_count += 1
        if clothes_in_box:
            capacity_of_rack = copy
            clothes_in_box.pop()

    elif capacity_of_rack < clothes_in_box[-1]:
        pass
