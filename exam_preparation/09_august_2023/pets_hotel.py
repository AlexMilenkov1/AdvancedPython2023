def accommodate_new_pets(available_capacity, max_weight_per_pet, *args):
    accommodation = {}
    successfully_accommodation = True
    result = []

    for info in args:
        pet_type = info[0]
        pet_weight = info[1]

        if available_capacity > 0:
            if pet_weight > max_weight_per_pet:
                continue
            if pet_type not in accommodation.keys():
                accommodation[pet_type] = 0
            accommodation[pet_type] += 1
            available_capacity -= 1
        else:
            successfully_accommodation = False
            break

    if successfully_accommodation:
        result.append(f"All pets are accommodated! Available capacity: {available_capacity}.")
    else:
        result.append("You did not manage to accommodate all pets!")

    result.append('Accommodated pets:')
    for pet, count in sorted(accommodation.items(), key=lambda kvp: kvp[0]):
        result.append(f'{pet}: {count}')

    return '\n'.join(result)


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
