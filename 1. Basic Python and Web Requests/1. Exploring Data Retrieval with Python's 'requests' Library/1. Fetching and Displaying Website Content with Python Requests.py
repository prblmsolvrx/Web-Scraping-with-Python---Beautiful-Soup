"""
In developing a web scraper for a project, you need to quickly test whether
your Python script can access a website and fetch its content. How would
you implement a simple script to fetch and display the first 500 characters
of a bookstore's HTML content using Python's requests library? Execute
the code below to see how this is accomplished on a popular bookstore's website.
"""

import requests

# Fetch content from a book store website
url = 'http://books.toscrape.com'
response = requests.get(url)

if response.ok:
    print("The book store website content was fetched successfully!")
    print(response.text[:500])  # Display the first 500 characters of the book store webpage content
else:
    print("Failed to fetch the book store website content.")