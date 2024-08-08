from bs4 import BeautifulSoup

# Assume this is the HTML from a section of a travel booking website
html_content = '''
<html>
  <body>
    <div class="destination">
      <h2 class="name">Sunny Beach</h2>
      <p class="description">A beautiful beach, perfect for family vacations.</p>
      <p class="price">Cost: $200</p>
    </div>
  </body>
</html>'''

# TODO: Create a BeautifulSoup object using `html_content` and 'html.parser' as parameters
soup = BeautifulSoup(html_content,'html.parser')

# TODO: Use BeautifulSoup methods and attributes to find the 'p' tag with class 'price' from the div
price_tag = soup.find('p',class_='price')

# TODO: Print the text content of the found 'p' tag
print(price_tag.text)

# Print the parent tag of the p tag you retrieved earlier
print(price_tag.parent)

"""
output:
Cost: $200
<div class="destination">
<h2 class="name">Sunny Beach</h2>
<p class="description">A beautiful beach, perfect for family vacations.</p>
<p class="price">Cost: $200</p>
</div>
"""