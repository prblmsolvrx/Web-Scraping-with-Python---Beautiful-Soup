"""
Great job understanding CSS selectors with BeautifulSoup!
For your next task, in the provided HTML content for an
online shopping site's inventory, you need to adjust the
code to print the names of the products instead of their prices.
Use your knowledge of CSS selec
"""
from bs4 import BeautifulSoup

# Simulated HTML content of an online shopping site's inventory
html_inventory = '''
<div id="inventory">
  <div class="product"><span class="name">Laptop</span> - <span class="price">$999</span></div>
  <div class="product"><span class="name">Phone</span> - <span class="price">$499</span></div>
  <div class="product"><span class="name">Tablet</span> - <span class="price">$299</span></div>
</div>
'''
soup = BeautifulSoup(html_inventory, 'html.parser')

# Select the price for each product
names = soup.select('.name')
for name in names:
    print(name.text)