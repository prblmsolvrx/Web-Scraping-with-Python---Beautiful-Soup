import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/tableful'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find("table")
rows = quotes.find_all("tr")[1:-1]

# TODO: Modify the code to extract only the first 2 quotes - note that the quotes are in every other row, since their tags are placed as a separate row
count = len(rows)

for i in range(0, 2, 2):
    quote = rows[i]
    tags_row = quote.find_next_sibling()
    tags = tags_row.find_all("a") if tags_row else []

    print("Quote: ", quote.text)
    for tag in tags:
        print("Tag: ", tag.text)

"""
output :-

Quote:  
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.” Author: Albert Einstein

Tag:  change
Tag:  deep-thoughts
Tag:  thinking
Tag:  world
"""