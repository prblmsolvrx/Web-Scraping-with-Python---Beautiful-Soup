import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_to_csv(base_url, start_page, filename):
    # Initialize an empty list to collect all quotes
    all_quotes = []

    # Set the current page to the start page
    current_page = start_page

    while current_page:
        # Retrieve the page content using requests.get
        response = requests.get(base_url + current_page)
        if response.status_code != 200:
            print(f"Failed to retrieve {current_page}")
            break
        
        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the quote elements on the page
        quotes = soup.find_all('div', class_='quote')

        # Loop through each quote element and extract the text, author, and tags
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
            all_quotes.append({'text': text, 'author': author, 'tags': tags})

        # Find the link to the next page and update the current page
        next_page = soup.find('li', class_='next')
        current_page = next_page.find('a')['href'] if next_page else None

    # Create a DataFrame from the collected data
    df = pd.DataFrame(all_quotes)

    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)

    # Print a confirmation message with the filename
    print(f"Data successfully saved to {filename}")

base_url = 'http://quotes.toscrape.com'
start_page = '/page/1/'
filename = 'quotes.csv'
extract_to_csv(base_url, start_page, filename)
