"""
 Expand on what you've learned by modifying the existing code
 to print the "Second Deal" from the travel deals section,
 using the .find_next_sibling() method. Remember,
 this method allows you to navigate horizontally in the HTML
 tree to find sibling elements.

"""
from bs4 import BeautifulSoup

# Simulating a section of an HTML document from a travel booking website
html_content = """
<div id='travel-deals'>
    <h2>Today's Top Deals</h2>
    <p>Save on flights to Hawaii!</p>
    <p>Discounted hotel rates in Paris!</p>
</div>
"""

# Creating a BeautifulSoup Object
soup = BeautifulSoup(html_content, 'html.parser')

# Find the 'h2' tag to see the section title
section_title = soup.find('h2').string
print("Section Title:", section_title)

# Find the first 'p' tag to see the first deal
first_deal = soup.find('p')

# TODO: Find the next sibling of the first 'p' tag (the second deal)
second_deal = first_deal.find_next_sibling('p')


# TODO: Remember to update the print statement below to print the second deal instead
print("Second Deal:", second_deal)