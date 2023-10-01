def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''

    for elements in sorted_cheese:
        result += f"{elements[0]}\n"
        sorted_result = sorted(elements[1], reverse=True)
        for cheese in sorted_result:
            result += f"{cheese}\n"

    return result


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

