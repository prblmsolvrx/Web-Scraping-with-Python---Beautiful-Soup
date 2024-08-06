"""
Your task is to modify the code to print the 'Content-Length'
of the response instead of 'Content-Type'. Remember, this header
tells us the size of the response body. Good luck, and let’s see
how well you understand the server's feedback through headers!
"""

import requests

# Making an HTTP GET request to fetch quotes
response = requests.get('http://quotes.toscrape.com')

# Only execute the following if the request was successful
if response.ok:
    # Print the 'Content-Type' header value
    # TODO: Update the code to fetch the Content-Length header
    print('Content-Type:', response.headers['Content-Type'])
    print('Content-Length:', response.headers['Content-Length'])

"""
output
Content-Type: text/html; charset=utf-8
Content-Length: 11054
"""