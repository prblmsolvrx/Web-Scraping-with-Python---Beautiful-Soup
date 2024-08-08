"""
 Extract the names of items from the provided HTML structure.
 Utilize your knowledge from the lesson on CSS selectors to
 identify paragraphs within divs classified as items in the inventory.
"""

from bs4 import BeautifulSoup

# HTML content for an online shopping site products inventory
html_content = '<div class="inventory"><div class="item"><p>Item 1</p></div><div class="item"><p>Item 2</p></div></div>'

# TODO: Use BeautifulSoup to parse the 'html_content' and create a soup object.
soup = BeautifulSoup(html_content,'html.parser')
# TODO: Using the soup object, find all paragraphs within divs classed as 'item'  within divs classified as 'inventory' using CSS selectors and print their text.
items = soup.select('.item')

for item in items:
    print(item.text)

"""
output
Item 1
Item 2
"""