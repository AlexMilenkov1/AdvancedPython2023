def fill_the_box(height, length, width, *args):
    size_of_box = height * length * width

    for i in range(len(args)):
        if args[i] == 'Finish':
            break

        size_of_box -= args[i]

    if size_of_box > 0:
        return f"There is free space in the box. You could put {size_of_box} more cubes."
    else:
        return f"No more free space! You have {abs(size_of_box)} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))