def concatenate(*args, **kwargs):
    string = ''

    for chars in args:
        string += chars

    for key, value in kwargs.items():
        if key in string:
            string = string.replace(key, value)

    return string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))