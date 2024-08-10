"""
Now, let's modify the script to also include the availability
status of each book. The availability status can be found
under the tag with the class instock availability.

Update the current code to include the availability
status in the output.

Before you proceed, let's understand how the CSS
selector works when the class name contains spaces
– when a class name contains spaces, it means that
the element has multiple classes. For example,
the class name instock availability means that
the element has two classes: instock and availability.
In this case, you can use the CSS selector .i
nstock.availability to select the element with both classes.
"""

from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books_ordered_list = soup.select(".page_inner section ol li")

for book in books_ordered_list:
    title = book.select("article h3 a")[0]["title"]
    availability = book.select("article .instock.availability")[0].text.strip()
    print(f"Title: {title}, Availability: {availability}")
