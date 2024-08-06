"""
Curious about what type of content a web server sends
when you request a webpage? The given code demonstrates
how to inspect the Content-Type header from the response
of a web server, using the example of http://quotes.toscrape.com.
This knowledge is valuable in web development for understanding
how to process the retrieved data. Run the code to see the type
of content provided by the server!
"""

import requests

# Checking the server's content type
url = 'http://quotes.toscrape.com'
response = requests.get(url)

if response.ok:
    content_type = response.headers.get('Content-Type', None)
    print("Content-Type: " + content_type) if content_type else print("Content-Type header missing!")

# output - Content-Type: text/html; charset=utf-8