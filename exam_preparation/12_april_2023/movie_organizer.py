def movie_organizer(*args):
    result = {}

    for info in args:
        movie = info[0]
        genre = info[1]

        if genre not in result.keys():
            result[genre] = []
        result[genre].append(movie)

    sorted_genres = dict(sorted(result.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    sorted_result = {}

    for genre, movies in sorted_genres.items():
        sorted_result[genre] = []
        sorted_result[genre] += sorted(movies)

    final_result = []

    for genre, movies in sorted_result.items():
        final_result.append(f'{genre} - {len(movies)}')
        for movie in movies:
            final_result.append(f'* {movie}')

    return '\n'.join(final_result)


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
