import requests
from bs4 import BeautifulSoup

def scrape_quotes(base_url):
    # Send a request to get the main page content
    response = requests.get(base_url)
    # Create a BeautifulSoup object from the response text
    soup = BeautifulSoup(response.text, 'html.parser')

    # Select all quotes on the main page
    quotes = soup.select('.quote')

    for quote in quotes:
        # Extract the text of the quote
        text = quote.select_one('.text').get_text()
        # Extract the author's name
        author = quote.select_one('.author').get_text()
        print(f'{text} - {author}')

        # Extract the relative URL to the author's page
        endpoint_to_about_page = quote.select_one('span a')['href']

        # Generate the full URL
        url_to_about_page = base_url + endpoint_to_about_page

        # Send a request to get the author's page content
        response = requests.get(url_to_about_page)

        # Create a BeautifulSoup object from the author's page
        soup_about = BeautifulSoup(response.text, 'html.parser')

        # TODO: Extract the author's birth date from the linked page using CSS selector and get it's text
        # Hint: The class name of the necessary elemenet is 'author-born-date'
        born_date = soup_about.select_one('.author-born-date').get_text()
        
        # TODO: Extract the author's birth location from the linked page using CSS selector and get it's text
        # Hint: The class name of the necessary elemenet is 'author-born-location'
        born_location = soup_about.select_one('.author-born-location').get_text()

        print(f'{author} was born on {born_date} in {born_location}\n')

base_url = 'http://quotes.toscrape.com'
scrape_quotes(base_url)