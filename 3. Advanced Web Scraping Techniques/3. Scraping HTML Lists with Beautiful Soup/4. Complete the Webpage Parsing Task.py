"""
Now, let's add a missing line, where we select the
li elements in the ordered list from the parsed
HTML using the CSS selector.
"""

from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Select the li elements in the ordered list from the parsed HTML using CSS selector
books_ordered_list = soup.select(".page_inner section ol li")

for book in books_ordered_list:
    title = book.select("article h3 a")[0]["title"]
    print(title)
