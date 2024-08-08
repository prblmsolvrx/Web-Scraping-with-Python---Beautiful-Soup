"""
The given code snippet accomplishes exactly that by utilizing BeautifulSoup
to parse HTML content. It targets specific elements based on their class
attributes to find all electronic products listed under the 'electronics'
category. Click Run to see which electronics are available!
"""

from bs4 import BeautifulSoup

# HTML snippet for an online shopping site with various product categories
html_content = "<div class='category-listing'><div class='electronics'><div class='product'>Smartphone</div><div class='product'>Laptop</div></div><div class='books'><div class='product'>Novel</div><div class='product'>Comics</div></div></div>"
soup = BeautifulSoup(html_content, 'html.parser')

# Using CSS selector to find all product elements within the 'electronics' category
electronics_products = soup.select(".category-listing > .electronics > .product")
for product in electronics_products:
    print(product.text)

"""
output:
Smartphone
Laptop
"""