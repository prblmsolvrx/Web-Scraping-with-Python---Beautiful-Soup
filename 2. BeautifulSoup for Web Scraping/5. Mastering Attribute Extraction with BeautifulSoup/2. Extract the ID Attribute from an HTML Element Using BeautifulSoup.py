"""
Your task is to modify the code to extract the id attribute from the second
<a> tag, instead of its href attribute. Use your knowledge of accessing
tag attributes with BeautifulSoup.
"""

from bs4 import BeautifulSoup

# Simulated HTML content
html_content = '<ul><li><a href="http://first-example.com" id="first">First example</a></li><li><a href="http://second-example.com" id="second">Second example</a></li></ul>'
soup = BeautifulSoup(html_content, 'html.parser')

# Extracting href attribute from the second a tag
second_link = soup.find('a', id="second")
href_second = second_link['id']
print(f"Second link extracted: {href_second}")