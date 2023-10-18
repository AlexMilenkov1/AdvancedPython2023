def forecast(*args):
    locations_weather = {}
    weather_order = {"Sunny": 0, "Cloudy": 1, "Rainy": 2}

    for info in args:
        location = info[0]
        weather = info[1]

        locations_weather[location] = weather

    sorted_locations = dict(sorted(locations_weather.items(), key=lambda kvp: (weather_order.get(kvp[1], float('inf')), kvp[0])))

    result = []

    for location, weather in sorted_locations.items():
        result.append(f'{location} - {weather}')

    return '\n'.join(result)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
