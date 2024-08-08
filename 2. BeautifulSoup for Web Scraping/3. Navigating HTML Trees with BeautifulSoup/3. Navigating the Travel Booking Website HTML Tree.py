"""
let's apply what you have learned about finding specific elements in an HTML structure.
Imagine you are extracting information from a travel booking website.
Can you complete the code to extract the price of the first travel package?

"""
from bs4 import BeautifulSoup

# Here is a sample HTML of a travel booking website
html_content = '''
<html>
<body>
<div class="package">
    <h1>Bali Adventure</h1>
    <p>Explore beautiful beaches and temples.</p>
    <p class="price">Only $999</p>
</div>
<div class="package">
    <h1>Paris Getaway</h1>
    <p>Visit the Eiffel Tower and museums.</p>
    <p class="price">Starting at $1399</p>
</div>
</body>
</html>'''

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find the first package div
first_package = soup.find('div', class_='package')

# Find the price within the first package
price = first_package.find('p', class_='price').string

# Print the first travel package price
print("First package price:", price)
