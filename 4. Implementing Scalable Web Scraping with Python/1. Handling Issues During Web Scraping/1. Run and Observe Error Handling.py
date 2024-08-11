import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'http://quotes.toscrape.com'

# Function to fetch the page content
def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.HTTPError as e:
        print(f"HTTP error: {e}")
        return None

# Function to parse and extract quote details
def parse_and_extract_quotes(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            try:
                text = quote.find('span', class_='text').get_text()
                author = quote.find('small', class_='author').get_text()
                tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
                print({'text': text, 'author': author, 'tags': tags})

                novels = quote.find_all('a', class_='novel').get_text()
                print(novels)
            except AttributeError as e:
                print(f"Attribute error encountered: {e}")
    except Exception as e:
        print(f"Parsing error: {e}")

# Fetch the page content
html = fetch_page(url)

if html:
    # Parse and extract quotes if the page content is successfully retrieved
    parse_and_extract_quotes(html)
else:
    print("An HTTP Error occurred.")