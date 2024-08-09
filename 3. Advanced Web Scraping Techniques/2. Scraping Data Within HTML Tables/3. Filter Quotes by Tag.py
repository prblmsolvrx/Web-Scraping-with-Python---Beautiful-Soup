"""
Change the given code to print only those quotes that have the tag life.
This way, you'll learn how to filter data based on specific criteria.
"""


import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/tableful'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find("table")
rows = quotes.find_all("tr")[1:-1]

# TODO: Print only those quotes that have the tag 'life'

for i in range(0, len(rows), 2):
    quote = rows[i]
    tags_row = quote.find_next_sibling()
    tags = tags_row.find_all("a") if tags_row else []

    tags_text = [tag.text for tag in tags]
    if 'life' in tags_text:
        print("Quote: ", quote.text)
        print("Tags: ", tags_text)


    
    