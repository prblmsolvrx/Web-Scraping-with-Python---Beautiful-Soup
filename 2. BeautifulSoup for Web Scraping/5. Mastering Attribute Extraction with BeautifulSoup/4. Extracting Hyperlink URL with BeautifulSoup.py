"""
Your mission is to extract a hyperlink URL from an anchor tag using BeautifulSoup.
Remember, focusing on extracting the href attribute from the <a> tag is key.
Use the BeautifulSoup library to parse HTML content and locate your target.
Ready to embark on the final challenge of this lesson? Let's showcase your web scraping skills!
"""

from bs4 import BeautifulSoup

# A sample HTML content containing an anchor with the 'href' attribute
html_content = '<a href="https://code.org" id="educational_link">Learn to Code!</a>'

# TODO: Create a 'soup' object using BeautifulSoup, passing 'html_content' and 'html.parser' as arguments
soup = BeautifulSoup(html_content,'html.parser')
# TODO: Find the anchor ('a') tag in 'soup' and store it in a variable 'anchor_tag'
anchor_tag_a = soup.find('a')
# TODO: Extract the 'href' attribute from 'anchor_tag' and print it
print(anchor_tag_a.get('href'))

"""
output: https://code.org
"""
