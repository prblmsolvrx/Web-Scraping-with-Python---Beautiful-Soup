import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'http://quotes.toscrape.com'

# Function to fetch the page content
def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.RequestException as e:
        print(f"HTTP Error: {e}")
        return None

# Function to parse and extract quote details
def parse_and_extract_quotes(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        quotes = []
        for quote in soup.find_all('div', class_='quote'):
            try:
                text = quote.find('span', class_='text').get_text(strip=True)
                author = quote.find('small', class_='author').get_text(strip=True)
                tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]
                quotes.append({
                    'text': text,
                    'author': author,
                    'tags': tags
                })
            except AttributeError as e:
                print(f"Missing attribute: {e}")
        return quotes
    except Exception as e:
        print(f"Parsing Error: {e}")
        return None

# Fetch the page content
html = fetch_page(url)

if html:
    # Parse and extract quotes if the page content is successfully retrieved
    quotes = parse_and_extract_quotes(html)
    if quotes:
        for quote in quotes:
            print(f"Quote: {quote['text']}")
            print(f"Author: {quote['author']}")
            print(f"Tags: {', '.join(quote['tags'])}")
            print('-' * 40)
    else:
        print("No quotes found.")
else:
    print("An HTTP Error occurred.")
