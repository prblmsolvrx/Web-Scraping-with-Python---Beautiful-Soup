"""
Python, let's fine-tune your skills.
This time, you're working with the HTML
content of an online shopping site.
Can you update the code to use a CSS selector that targets
all elements containing product name and print their
text content? Remember the lessons about CSS selectors
to select the correct HTML elements.
"""

from bs4 import BeautifulSoup

# HTML content for an online shopping site with a list of products
html_content = '<div><p class="price">Price: $50</p><p class="product-name">Widget A</p></div><div><p class="price">Price: $75</p><p class="product-name">Widget B</p></div>'
soup = BeautifulSoup(html_content, 'html.parser')

# TODO: Retrieve all the product names using appropriate CSS selector with soup.select method

product_names = soup.select('.product-name')

for pname in product_names:
    print(pname.text)

"""
output
Widget A
Widget B
"""