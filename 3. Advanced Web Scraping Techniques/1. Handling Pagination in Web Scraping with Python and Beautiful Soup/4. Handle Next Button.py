"""
Now, let's add the missing piece to our
web scraping script. We need to get the
URL of the next page from the "Next"
button on the page.

Follow the TODO in the starter code
to complete the task.
"""

import requests
from bs4 import BeautifulSoup

base_url = 'http://quotes.toscrape.com'
next_url = '/page/1/'
while next_url:
    response = requests.get(f"{base_url}{next_url}")
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        print(f"{text} by {author}")

    # TODO: Add code to get the button that leads to the next page. It is a list item with the class "next"
    next_button = soup.find("li",class_="next")
    next_url = next_button.find("a")["href"] if next_button else None