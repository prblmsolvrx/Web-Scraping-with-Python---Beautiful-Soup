"""
fill in the missing part of the code to have a delay
to not overwhelm the server.
"""

import requests
from bs4 import BeautifulSoup
import time

def scrape_heroes(base_url, first_page):
    next_page = first_page
    while next_page:
        try:
            response = requests.get(base_url + next_page, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
        for hero in soup.select(".quote"):
            name = hero.select_one(".text").get_text(strip=True)
            power = hero.select_one(".author").get_text(strip=True)
            print(f"'{name}' has power: {power}")

        next_page_link = soup.select_one("li.next > a")
        next_page = next_page_link["href"] if next_page_link else None
        
        # TODO: Add wait time of 1 second before continuing the scraping to not overwhelm the server
        time.sleep(1)
        print("\n")

base_url = 'http://quotes.toscrape.com'
first_page = '/page/1/'
scrape_heroes(base_url, first_page)