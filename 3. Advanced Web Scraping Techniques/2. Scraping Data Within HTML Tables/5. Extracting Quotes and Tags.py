"""
In this task, you need to fill in the missing parts of the
code to extract table data and rows from the HTML content.
"""

import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/tableful'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# TODO: Extract the table element from the HTML content

table = soup.find('table')

# TODO: Extract the rows from the table element, excluding the header and footer rows (first and last rows) and store the result in a variable called `rows`

rows = table.find_all('tr')[1:-1]

for i in range(0, len(rows), 2):
    quote = rows[i]
    tags_row = quote.find_next_sibling()
    tags = tags_row.find_all("a") if tags_row else []

    print("Quote: ", quote.text)
    for tag in tags:
        print("Tag: ", tag.text)