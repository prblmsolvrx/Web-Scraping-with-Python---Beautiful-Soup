import requests
from bs4 import BeautifulSoup

base_url = 'http://quotes.toscrape.com'
next_url = '/page/1/'

# TODO: Create a while loop that continues as long as next_url is not None
while next_url:
    # TODO: Make a request to the current page and get its content
    response = requests.get(f"{base_url}{next_url}")
    
    # TODO: Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # TODO: Find all quotes on the page and print each quote's text - Quotes are inside a div with class "quote"
    quotes = soup.find_all("div", class_="quote")
    
    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        print(f"{text} - {author}")
    
    # TODO: Find the "Next" button and get the URL for the next page - The "Next" button is inside a li with class "next"
    next_button = soup.find("li", class_="next")
    next_url = next_button.find("a")["href"] if next_button else None