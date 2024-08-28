from scraper import Scraper
from team import Team
from filters import TeamFilter

def get_user_choice():
    while True:
        print("How would you like to filter the teams?")
        print("1. Team name")
        print("2. Year")
        print("3. Number of wins")
        print("4. Exit")
        choice = input("Select a filter type (1/2/3) or exit (4): ")
        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

def filter_teams(teams):
    choice = get_user_choice()

    if choice == "1":
        name_query = input("Enter the team name or part of it: ")
        filtered_teams = TeamFilter.filter_by_name(teams, name_query)
    elif choice == "2":
        while True:
            year = input("Enter the year (e.g., 1990): ")
            if year.isdigit():
                filtered_teams = TeamFilter.filter_by_year(teams, year)
                break
            else:
                print("Invalid year. Please enter a valid number.")
    elif choice == "3":
        while True:
            try:
                min_wins = int(input("Enter the minimum number of wins: "))
                filtered_teams = TeamFilter.filter_by_wins(teams, min_wins)
                break
            except ValueError:
                print("Invalid number. Please enter a valid number.")
    elif choice == "4":
        print("Exiting the program.")
        return None
    
    return filtered_teams

def print_teams(teams):
    if teams:
        print(f"{'Team name':<30} {'Year':<10} {'Wins':<10} {'Losses':<10}")
        for team in teams:
            print(team)
    else:
        print("No results found based on the provided filter criteria.")

if __name__ == "__main__":
    scraper = Scraper(per_page=100)
    teams_data = scraper.scrape_all_pages()
    
    teams = [Team(**team) for team in teams_data]
    
    while True:
        filtered_teams = filter_teams(teams)
        if filtered_teams is None:
            break
        print_teams(filtered_teams)
        print("\n---\n")
