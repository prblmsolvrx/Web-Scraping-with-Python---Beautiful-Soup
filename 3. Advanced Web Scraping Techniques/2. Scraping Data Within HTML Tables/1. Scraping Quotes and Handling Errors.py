"""
First, we will fetch the webpage content and parse
it using BeautifulSoup.
Then, we will locate and extract rows from an HTML table.
Finally, we will loop through the rows, extracting
and printing quote texts and their associated tags.
"""

import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/tableful'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find("table")
rows = quotes.find_all("tr")[1:-1]

for i in range(0, len(rows), 2):
    quote = rows[i]
    tags_row = quote.find_next_sibling()
    tags = tags_row.find_all("a") if tags_row else []

    print("Quote: ", quote.text)
    for tag in tags:
        print("Tag: ", tag.text)