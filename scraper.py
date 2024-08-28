import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, per_page):
        self.per_page = per_page
        self.page_number = 1

    def generate_url(self):
        return f"https://www.scrapethissite.com/pages/forms/?page_num={self.page_number}&per_page={self.per_page}"

    def fetch_page_content(self, url):
        response = requests.get(url)
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, "html.parser")

    def has_next_page(self, soup):
        pagination = soup.find('ul', class_='pagination')
        if pagination:
            pages = pagination.find_all('li')
            last_page = pages[-1]
            return 'disabled' not in last_page.get('class', [])
        return False

    def scrape_all_pages(self):
        all_teams = []
        while True:
            url = self.generate_url()
            soup = self.fetch_page_content(url)
            statistics = soup.find_all(class_='team')
            if not statistics:
                break

            all_teams.extend(self.extract_team_data(statistics))

            if not self.has_next_page(soup):
                break

            self.page_number += 1

        return all_teams

    def extract_team_data(self, statistics):
        teams = []
        for team in statistics:
            team_name = team.find('td', class_='name').text.strip()
            year = team.find('td', class_='year').text.strip()
            wins = team.find('td', class_='wins').text.strip()
            losses = team.find('td', class_='losses').text.strip()
            teams.append({
                "name": team_name,
                "year": year,
                "wins": wins,
                "losses": losses
            })
        return teams
