import matplotlib.pyplot as plt

def plot_wins_over_time(teams, team_name):
    filtered_teams = [team for team in teams if team.name.lower() == team_name.lower()]
    
    if not filtered_teams:
        print(f"No data found for team: {team_name}")
        return

    years = [int(team.year) for team in filtered_teams]
    wins = [int(team.wins) for team in filtered_teams]

    plt.figure(figsize=(10, 5))
    plt.plot(years, wins, marker='o', linestyle='-', color='b')
    plt.xlabel('Year')
    plt.ylabel('Number of Wins')
    plt.title(f'Number of Wins Over Time for {team_name}')
    plt.grid(True)
    plt.show()

def plot_multiple_teams_over_time(teams, team_names):
    plt.figure(figsize=(10, 5))

    for team_name in team_names:
        filtered_teams = [team for team in teams if team.name.lower() == team_name.lower()]
        
        if not filtered_teams:
            print(f"No data found for team: {team_name}")
            continue

        years = [int(team.year) for team in filtered_teams]
        wins = [int(team.wins) for team in filtered_teams]

        plt.plot(years, wins, marker='o', linestyle='-', label=team_name)

    plt.xlabel('Year')
    plt.ylabel('Number of Wins')
    plt.title('Team Performance Comparison Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()