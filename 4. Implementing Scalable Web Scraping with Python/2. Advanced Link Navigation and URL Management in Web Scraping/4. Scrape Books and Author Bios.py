"""
Awesome work on the previous tasks!
Now, let's shift to the books scraping in this exercise.
In this task, we are scraping the books page,
then navigating to each individual book page
and retrieving information for each book
Follow the TODO instructions to complete
the task to fetch the necessary information
for each book as a product.
"""

import requests
from bs4 import BeautifulSoup

def parse_product_info(product_page_url):
    product_html = requests.get(product_page_url)
    product_soup = BeautifulSoup(product_html.text, 'html.parser')

    table = product_soup.select_one(".table.table-striped")

    info = {}

    if table:
        rows = table.find_all('tr')
        
        for row in rows:
            header = row.find('th')
            data = row.find('td')

            if header and data:
                key = header.text.strip()
                value = data.text.strip()
                info[key] = value

    return info

def scrape_books(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.select('.product_pod')

    for book in books:
        title = book.select_one('h3 a')['title']
        author_page_endpoint = book.select_one('h3 a')['href']
        product_page_url = base_url + author_page_endpoint

        info = parse_product_info(product_page_url)

        print(f'Book: {title}')
        print(f'Info: {info}')

base_url = 'http://books.toscrape.com/'
scrape_books(base_url)
