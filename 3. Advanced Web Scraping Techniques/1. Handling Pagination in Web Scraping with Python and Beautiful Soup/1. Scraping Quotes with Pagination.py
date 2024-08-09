import requests
from bs4 import BeautifulSoup

base_url = 'http://quotes.toscrape.com'
next_url = '/page/1/'
while next_url:
    response = requests.get(f"{base_url}{next_url}")
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        print(quote.find("span", class_="text").text)

    next_button = soup.find("li", class_="next")
    next_url = next_button.find("a")["href"] if next_button else None