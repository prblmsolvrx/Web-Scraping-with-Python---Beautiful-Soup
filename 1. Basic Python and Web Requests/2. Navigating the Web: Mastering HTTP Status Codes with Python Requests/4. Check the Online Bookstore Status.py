"""
check if an online bookstore is open by making a web request to its site.
Use Python's requests library to send a GET request to 'http://quotes.toscrape.com'.
Based on the HTTP status code returned, you will print messages to indicate whether
the bookstore is open or if there was an issue. Remember, a status code of 200 means success,
404 indicates "not found," and any other status means an error occurred.
This is your chance to showcase what you've learned about handling HTTP status codes!
"""

import requests

# TODO: Make a GET request to the online bookstore at http://quotes.toscrape.com
url = "http://quotes.toscrape.com"
# TODO: Check the HTTP status code of the response
# If it's 200, print a message indicating success
# If it's 404, indicate the page was not found
# Otherwise, indicate an error occurred
response = requests.get(url)
if response.status_code == 200:
    print("success")
elif response.status_code == 404:
    print("message not found")
