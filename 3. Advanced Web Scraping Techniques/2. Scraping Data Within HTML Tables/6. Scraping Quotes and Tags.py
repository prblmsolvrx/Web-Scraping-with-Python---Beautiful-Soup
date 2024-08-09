"""
Your task is to scrape quotes and corresponding tags
from an HTML table on a webpage. Remember,
only analyzing the HTML structure of the page
will help you identify the correct tags to scrape.
"""

import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/tableful'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Locate/extract the HTML table
table = soup.find('table')

# Extract all rows from the table (excluding the header row)
rows = table.find_all('tr')[1:]  # Skip the header row

# Loop through rows to extract quote text and tags
for row in rows:
    cells = row.find_all('td')
    if len(cells) == 3:  # Ensure the row has the expected number of columns
        quote_text = cells[0].get_text(strip=True)
        tags = cells[2].get_text(strip=True).split(', ')
        print(f"Quote: {quote_text}")
        print(f"Tags: {tags}")
        print('---')

