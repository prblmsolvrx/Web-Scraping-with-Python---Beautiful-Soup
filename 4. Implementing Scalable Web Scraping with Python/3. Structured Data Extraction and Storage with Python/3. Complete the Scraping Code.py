"""
Great work so far!
In this task, you'll fill in the missing parts of the code needed to extract quotes from a website and save them in a CSV file.
The function extract_to_csv retrieves HTML content, parses it to find quotes, authors, and tags, and stores the data in a structured format.
Your job is to complete the TODO sections of the given code.
Remember to check out the quotes.csv file to observe the saved data after running the code.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_to_csv(base_url, start_page, filename):
    all_quotes = []
    current_page = start_page

    while current_page:
        response = requests.get(f"{base_url}{current_page}")  # Get the page content
        soup = BeautifulSoup(response.text, 'html.parser')   # Parse the HTML content

        quotes = soup.find_all('div', class_='quote')  # Find all quote blocks

        for quote in quotes:
            text = quote.find('span', class_='text').get_text()  # Extract the quote text
            author = quote.find('span', class_='author').get_text()  # Extract the author name
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]  # Extract tags
            all_quotes.append({"text": text, "author": author, "tags": tags})  # Append the quote data

        next_link = soup.find('li', class_='next')  # Find the next page link
        current_page = next_link.find('a')['href'] if next_link else None  # Update the current page

    # Create Pandas DataFrame with all_quotes
    df = pd.DataFrame(all_quotes)

    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

base_url = 'http://quotes.toscrape.com'
start_page = '/page/1/'
filename = 'quotes.csv'
extract_to_csv(base_url, start_page, filename)
