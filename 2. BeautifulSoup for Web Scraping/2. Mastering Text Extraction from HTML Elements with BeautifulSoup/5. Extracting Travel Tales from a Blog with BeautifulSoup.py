"""
Create a Python script that simulates the extraction
of text from the paragraphs of a travel blog.
Your goal is to find all paragraph tags in the given
HTML content, extract, and print their text.
"""


from bs4 import BeautifulSoup

# Simulating the HTML content of a travel blog
html_content = "<div><p>Exploring the ancient temples of Cambodia.</p><p>Unforgettable sunrise at Angkor Wat!</p></div>"

# TODO: Use BeautifulSoup to parse 'html_content'.
soup = BeautifulSoup(html_content, 'html.parser')
# TODO: Find all paragraph tags ('p') and iterate over them to print the text of each paragraph.
paragraphs = soup.find_all('p')

for paragraph in paragraphs:
    print(paragraph.text)
    
    