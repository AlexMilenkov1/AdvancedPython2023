def team_lineup(*args):
    result = {}

    for info in args:
        player_name = info[0]
        country = info[1]

        if country not in result.keys():
            result[country] = []
        result[country].append(player_name)

    sorted_result = dict(sorted(result.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    final_result = []

    for country, players in sorted_result.items():
        final_result.append(f'{country}:')
        for player in players:
            final_result.append(f'  -{player}')

    return '\n'.join(final_result)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
