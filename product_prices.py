import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/forms/?q=&per_page=25"
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, "html.parser")

statistics = soup.find_all(class_='team')
print(statistics)
