"""
Find and Print Navigation Links: In this exercise,
you are tasked with identifying navigation links
(a tags with the class nav) in HTML content and printing their href attributes.
Focus on applying BeautifulSoup methods to efficiently extract relevant attributes.
"""

from bs4 import BeautifulSoup

# Assume we have HTML content with multiple links
html_content = '<div><a href="http://example.com/page1" class="nav">Page 1</a><a href="http://example.com/page2" class="nav">Page 2</a></div>'
soup = BeautifulSoup(html_content, 'html.parser')

# TODO: Retrieve all 'a' tags with a class of 'nav'. Remember how to use find_all for this.
nav_links = soup.find_all('a', class_='nav')

for link in nav_links:
    # TODO: Extract and print the 'href' attribute
    print(link.get('href'))

"""
output :-
http://example.com/page1
http://example.com/page2
"""