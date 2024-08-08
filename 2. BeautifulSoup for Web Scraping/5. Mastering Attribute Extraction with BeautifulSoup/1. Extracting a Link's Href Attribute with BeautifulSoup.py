from bs4 import BeautifulSoup

html_content = '<a href="http://quotes.toscrape.com" id="quote_link">Inspiring Quotes</a>'
soup = BeautifulSoup(html_content, 'html.parser')

# Extracting href attribute from the a tag
quote_link = soup.find('a')
href_value = quote_link['href']
print(f"Href extracted: {href_value}")

"""
output: 
Href extracted: http://quotes.toscrape.com
"""