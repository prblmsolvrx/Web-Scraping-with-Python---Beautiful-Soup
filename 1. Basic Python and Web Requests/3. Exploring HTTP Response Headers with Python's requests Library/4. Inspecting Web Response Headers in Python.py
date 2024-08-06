"""
Use the skills you've honed to make a request to http://quotes.toscrape.com, check if the response is successful,
and fetch a specific header value. Remember, headers offer valuable insights into the behavior and expectations of web servers.
"""

import requests

# TODO: Make a GET request to the website (http://quotes.toscrape.com) and store the response
response = requests.get('http://quotes.toscrape.com')
# TODO: Check if the request was successful (use the 'ok' property)
# TODO: Print the 'Content-Type' header from the response
if response.ok:
    print("Content-type:",response.headers['Content-Type'])
