import requests
from bs4 import BeautifulSoup

# TODO: Define the function scrape_quotes(base_url)
# TODO: Send a request to the main URL and get the page content
# TODO: Create a BeautifulSoup object from the response text
# TODO: Find all quotes in the main page using the appropriate CSS selector
# TODO: Iterate over each quote and extract the text and author
# TODO: For each quote, find the relative URL to the author's page
# TODO: Create the full URL to the author's page by concatenating it with the base URL
# TODO: Send a request to the author's page URL
# TODO: Create a BeautifulSoup object from the author's page content
# TODO: Extract the author's birth date
# TODO: Extract the author's birth location
# TODO: Print the author's name, birth date, and birth location

def scrape_quotes(base_url):
    response = requests.get(base_url)
    # Send a request to the main URL and get the page content
    if response.status_code != 200:
        print(f"Failed to retrive the page : {response.status_code}")
        return
        
    # Create a BeautifulSoup object from the response text
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all quotes in the main page using the appropriate CSS selector
    quotes = soup.select('.quote')
    
    for quote in quotes:
        # Extract the quote text and author
        text = quote.select_one('.text').get_text()
        author = quote.select_one('.author').get_text()

        # Find the relative URL to the author's page
        author_url = quote.select_one('.author + a')['href']
        
        # Create the full URL to the author's page by concatenating it with the base URL
        author_page_url = base_url + author_url
        
        # Send a request to the author's page URL
        author_response = requests.get(author_page_url)
        if author_response.status_code != 200:
            print(f"Failed to retrieve the author's page. Status code: {author_response.status_code}")
            continue
        
        # Create a BeautifulSoup object from the author's page content
        author_soup = BeautifulSoup(author_response.text, 'html.parser')
        
        # Extract the author's birth date
        birth_date = author_soup.select_one('.author-born-date').get_text()
        
        # Extract the author's birth location
        birth_location = author_soup.select_one('.author-born-location').get_text()
        
        # Print the author's name, birth date, and birth location
        print(f"Author: {author}")
        print(f"Birth Date: {birth_date}")
        print(f"Birth Location: {birth_location}")
        print()


base_url = 'http://quotes.toscrape.com'
scrape_quotes(base_url)