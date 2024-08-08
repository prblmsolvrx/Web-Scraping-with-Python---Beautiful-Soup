from bs4 import BeautifulSoup

# Given HTML content from the travel blog website scenario
html_content = '''
<div>
    <p>Welcome to my travel blog. Here are my adventures:</p>
    <p>Day 1: I've arrived in Paris, and the Eiffel Tower is stunning!</p>
    <p>Day 2: The Louvre was amazing, so much to see.</p>
</div>
'''
soup = BeautifulSoup(html_content, 'html.parser')

# Print out all the texts within paragraph tags
for paragraph in soup.find_all('p'):
    print(paragraph.text)

# output

"""
Welcome to my travel blog. Here are my adventures:
Day 1: I've arrived in Paris, and the Eiffel Tower is stunning!
Day 2: The Louvre was amazing, so much to see.
"""