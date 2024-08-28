class TeamFilter:
    @staticmethod
    def filter_by_name(teams, name_query):
        return [team for team in teams if name_query.lower() in team.name.lower()]

    @staticmethod
    def filter_by_year(teams, year):
        return [team for team in teams if team.year == str(year)]

    @staticmethod
    def filter_by_wins(teams, min_wins):
        return [team for team in teams if int(team.wins) >= min_wins]
