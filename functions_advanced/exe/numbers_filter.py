def even_odd_filter(**kwargs):
    result_dict = {}

    for key in kwargs.keys():
        if key == 'even':
            result_dict['even'] = []
            result_dict['even'] += list(filter(lambda x: x % 2 == 0, kwargs[key]))
        if key == 'odd':
            result_dict['odd'] = []
            result_dict['odd'] += list(filter(lambda x: x % 2 != 0, kwargs[key]))

    return dict(sorted(result_dict.items(), key=lambda kvp: -len(kvp)))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
