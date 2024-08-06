"""
You'll need to make a request to a website and check a
specific type of header. Can you figure out how to
retrieve the 'Content-Type' from the response headers by yourself?
"""

import requests

response = requests.get('http://quotes.toscrape.com')
if response.ok:
    # TODO: Retrieve and print the 'Content-Type' header from the response
    print('Content-Type:',response.headers['Content-Type'])

"""
output:- 
Content-Type: text/html; charset=utf-8
"""