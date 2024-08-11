import requests
from bs4 import BeautifulSoup

def scrape_quotes(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.select('.quote')

    for quote in quotes:
        text = quote.select_one('.text').get_text()
        author = quote.select_one('.author').get_text()
        print(f'{text} - {author}')

        endpoint_to_about_page = quote.select_one('span a')['href']
        url_to_about_page = base_url + endpoint_to_about_page

        response = requests.get(url_to_about_page)
        soup_about = BeautifulSoup(response.text, 'html.parser')
        born_date = soup_about.select_one('.author-born-date').get_text()
        born_location = soup_about.select_one('.author-born-location').get_text()

        # Remove leading "in " from born_location if present
        if born_location.startswith("in "):
            born_location = born_location[3:]

        print(f'{author} was born on {born_date} in {born_location}\n')

base_url = 'http://quotes.toscrape.com'
scrape_quotes(base_url)