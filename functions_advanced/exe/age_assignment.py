def age_assignment(*args, **kwargs):
    info = {}

    for i in range(len(args)):
        info[args[i]] = kwargs[args[i][0]]

    sorted_info = dict(sorted(info.items(), key=lambda kvp: kvp[0]))

    result = []

    for name, age in sorted_info.items():
        result.append(f"{name} is {age} years old.")

    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))