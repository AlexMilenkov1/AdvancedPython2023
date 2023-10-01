def get_info(**kwargs):

    result = f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old"

    return result


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
