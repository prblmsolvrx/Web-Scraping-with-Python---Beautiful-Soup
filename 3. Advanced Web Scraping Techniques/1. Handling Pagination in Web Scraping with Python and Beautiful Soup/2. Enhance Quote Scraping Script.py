"""
Currently, the code prints only the text of the quotes.
Change the code to also print the author of each quote.
Remember, analyzing the structure of the page is
crucial in web scraping. So, if you are not sure where
to find the author's name, you can open the URL in
another tab and inspect the page.
"""

# Import the requests library to make HTTP requests
import requests
# Import BeautifulSoup from bs4 library for parsing HTML
from bs4 import BeautifulSoup

# Set the base URL of the website we're scraping
base_url = 'http://quotes.toscrape.com'
# Initialize the next_url variable with the first page to scrape
next_url = '/page/1/'

# Start a loop that continues as long as there's a next page to scrape
while next_url:
    # Make a GET request to the current page
    response = requests.get(f"{base_url}{next_url}")
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all div elements with class "quote" (these contain the quotes)
    quotes = soup.find_all("div", class_="quote")


# TODO: Modify the code to print the author of each quote along with the text
    # Loop through each quote found on the page
    for quote in quotes:
        # Find and print the text of the quote (in a span with class "text")
        print(quote.find("span", class_="text").text)
        # Find and print the author of the quote (in a small tag with class "author")
        print(quote.find("small", class_="author").text)

    # Look for the "next" button to find the URL of the next page
    next_button = soup.find("li", class_="next")
    # If there's a next button, get its href attribute; otherwise, set next_url to None
    next_url = next_button.find("a")["href"] if next_button else None
    

