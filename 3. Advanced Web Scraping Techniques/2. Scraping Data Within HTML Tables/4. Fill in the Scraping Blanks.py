import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/tableful'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find("table")
rows = quotes.find_all("tr")[1:-1]

for i in range(0, len(rows), 2):
    quote_row = rows[i]
    quote_text = quote_row.find("td").text  # Extract quote from <td> tags
    
    tags_row = quote_row.find_next_sibling("tr")
    tag_elements = tags_row.find_all("a") if tags_row else []
    tags = [tag.text for tag in tag_elements]
    
    print("Quote: ", quote_text)
    for tag in tags:
        print("Tag: ", tag)
    print()  # Print a blank line for clarity
