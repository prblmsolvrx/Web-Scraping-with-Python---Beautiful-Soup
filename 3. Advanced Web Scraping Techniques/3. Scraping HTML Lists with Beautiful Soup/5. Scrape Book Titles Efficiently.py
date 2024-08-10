"""
In this exercise, some parts of the code are missing.
Your task is to fill in the missing blocks to complete 
he script. This practice will strengthen your understanding
of using CSS selectors.

Complete the code to print the titles of the books
listed on the webpage.
"""

from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books_ordered_list = soup.select(".page_inner section ol li")

for book in books_ordered_list:
    # Select 'a' tags in the 'h3' element in the 'article' and extract the 'title' attribute
    title_tag = book.select("article h3 a")[0]
    title = title_tag["title"]
    print(title)
