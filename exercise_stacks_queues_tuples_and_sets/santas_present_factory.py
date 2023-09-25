from collections import deque

boxes_with_materials = deque(int(x) for x in input().split())
magic_values = deque(int(x) for x in input().split())

doll_made_count = 0
wooden_train_made_count = 0
teddy_bear_made_count = 0
bicycle_made_count = 0

while boxes_with_materials and magic_values:
    calculation = boxes_with_materials[-1] * magic_values[0]

    if calculation == 150:
        doll_made_count += 1
        boxes_with_materials.pop()
        magic_values.popleft()

    elif calculation == 250:
        wooden_train_made_count += 1
        boxes_with_materials.pop()
        magic_values.popleft()

    elif calculation == 300:
        teddy_bear_made_count += 1
        boxes_with_materials.pop()
        magic_values.popleft()

    elif calculation == 400:
        bicycle_made_count += 1
        boxes_with_materials.pop()
        magic_values.popleft()

    else:
        if boxes_with_materials[-1] == 0 and magic_values[0] == 0:
            boxes_with_materials.pop()
            magic_values.popleft()
            continue

        if boxes_with_materials[-1] == 0:
            boxes_with_materials.pop()
            continue

        if magic_values[0] == 0:
            magic_values.popleft()
            continue

        if calculation < 0:
            sum_values = magic_values[0] + boxes_with_materials[-1]
            boxes_with_materials.pop()
            magic_values.popleft()
            boxes_with_materials.append(sum_values)

        elif calculation > 0:
            magic_values.popleft()
            boxes_with_materials[-1] += 15


if doll_made_count >= 1 and wooden_train_made_count >= 1:
    print('The presents are crafted! Merry Christmas!')
elif teddy_bear_made_count >= 1 and bicycle_made_count >= 1:
    print('The presents are crafted! Merry Christmas!')
else:
    print("No presents this Christmas!")

if boxes_with_materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(boxes_with_materials))}")
if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

if bicycle_made_count >= 1:
    print(f'Bicycle: {bicycle_made_count}')
if doll_made_count >= 1:
    print(f'Doll: {doll_made_count}')
if teddy_bear_made_count >= 1:
    print(f'Teddy bear: {teddy_bear_made_count}')
if wooden_train_made_count >= 1:
    print(f'Wooden train: {wooden_train_made_count}')
