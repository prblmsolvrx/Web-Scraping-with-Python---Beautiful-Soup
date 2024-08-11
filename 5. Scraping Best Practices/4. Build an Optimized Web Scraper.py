# TODO: Define the function scrape with parameters base_url and start_page
# TODO: Initialize the variable current_page with start_page
# TODO: Create a while loop that runs as long as current_page is not None
# TODO: Use try-except block to handle exceptions from HTTP requests
# TODO: Make a GET request to the current page with a timeout of 10 seconds
# TODO: Raise an HTTP error if the request was unsuccessful
# TODO: Parse the HTML content of the response using BeautifulSoup
# TODO: Use a for loop to iterate over all quotes on the page
# TODO: Extract the text of each quote using the CSS selector '.text'
# TODO: Extract the author of each quote using the CSS selector '.author'
# TODO: Print the quote text and author in the format: "'<text>' by <author>"
# TODO: Find the link to the next page using the CSS selector 'li.next > a'
# TODO: Update current_page to the href attribute of the next page link or None if not found
# TODO: Add a delay of 1 second between requests using time.sleep(1)
# TODO: Print a newline character for better readability in the output

import requests
from bs4 import BeautifulSoup
import time

def scrape(base_url, start_page):
    current_page = start_page
    
    while current_page is not None:
        try:
            # Make a GET request to the current page with a timeout of 10 seconds
            response = requests.get(base_url + current_page, timeout=10)
            response.raise_for_status()  # Raise an HTTP error if the request was unsuccessful
            
            # Parse the HTML content of the response using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Iterate over all quotes on the page
            for quote in soup.select('.quote'):
                # Extract the text of each quote using the CSS selector '.text'
                text = quote.select_one('.text').get_text()
                # Extract the author of each quote using the CSS selector '.author'
                author = quote.select_one('.author').get_text()
                # Print the quote text and author
                print(f"'{text}' by {author}")
            
            # Find the link to the next page using the CSS selector 'li.next > a'
            next_page = soup.select_one('li.next > a')
            if next_page:
                # Update current_page to the href attribute of the next page link
                current_page = next_page['href']
            else:
                # If no next page is found, set current_page to None to stop the loop
                current_page = None
            
            # Add a delay of 1 second between requests
            time.sleep(1)
            # Print a newline character for better readability in the output
            print()
        
        except Exception as e:
            print(f"An error occurred: {e}")
            break

base_url = 'http://quotes.toscrape.com'
start_page = '/page/1/'
scrape(base_url, start_page)
