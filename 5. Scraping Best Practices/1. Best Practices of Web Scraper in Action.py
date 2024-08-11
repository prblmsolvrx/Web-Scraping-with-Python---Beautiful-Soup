"""
Great progress so far! Now, let's run a Python script that demonstrates best practices for web scraping. The script scrapes quotes from a website, collecting content from multiple pages while respecting the server.
This script uses:
Requests and BeautifulSoup: For fetching and parsing web page content.
Timeouts: To ensure the scraper doesn't hang indefinitely.
Error Handling: To manage request errors gracefully.
Polite Crawling: Adding delays between requests using time.sleep().
Navigation: Handling multiple pages by detecting "Next" page links.
When you run this code, it will print each quote's text and author name. Pay attention to how errors are handled, how pages are navigated, and how the server is respected by limiting requests.
"""

import requests
from bs4 import BeautifulSoup
import time

def scrape(base_url, start_page):
    current_page = start_page
    while current_page:
        try:
            response = requests.get(base_url + current_page, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        for quote in soup.select(".quote"):
            text = quote.select_one(".text").get_text(strip=True)
            author = quote.select_one(".author").get_text(strip=True)
            print(f"'{text}' by {author}")

        next_page = soup.select_one("li.next > a")
        current_page = next_page["href"] if next_page else None
        time.sleep(1)  # Respectful crawling by sleeping for 1 second
        print("\n")

base_url = 'http://quotes.toscrape.com'
start_page = '/page/1/'
scrape(base_url, start_page)