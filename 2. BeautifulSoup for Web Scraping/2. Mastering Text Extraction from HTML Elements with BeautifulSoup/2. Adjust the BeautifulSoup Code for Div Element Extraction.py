"""
Fantastic progress! For your next challenge,
switch the focus from extracting all paragraph
elements to fetching the entire div element,
including its nested paragraphs. Adjust the code
to extract and print the div content,
exploring how different tag selections impact your results.
"""

from bs4 import BeautifulSoup

html_content = "<div><p>Amazing travel destinations:</p><p>Paris, France</p><p>Bali, Indonesia</p></div>"
soup = BeautifulSoup(html_content, 'html.parser')
paragraphs = soup.find_all('div')

for paragraph in paragraphs:
    print(paragraph.text)