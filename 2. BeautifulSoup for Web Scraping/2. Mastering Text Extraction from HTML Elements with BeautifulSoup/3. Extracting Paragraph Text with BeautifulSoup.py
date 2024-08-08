"""
Extracting Paragraph Text with BeautifulSoup
"""

from bs4 import BeautifulSoup

# Imagine an HTML page of a travel blog where paragraphs describe various travel experiences
html_content = "<div><p>The Alps are breathtaking!</p><p>Paris is romantic.</p><p>Tokyo is bustling with energy.</p></div>"

# Create a soup object to parse the given HTML
soup = BeautifulSoup(html_content, 'html.parser')

# TODO: Find all paragraph ('p') tags from the soup object and then print the text of each paragraph.
paragraphs = soup.find_all('p')

for paragraph in paragraphs:
    print(paragraph.text)
