class Team:
    def __init__(self, name, year, wins, losses):
        self.name = name
        self.year = year
        self.wins = wins
        self.losses = losses

    def __repr__(self):
        return f"{self.name:<30} {self.year:<10} {self.wins:<10} {self.losses:<10}"
