"""
Great job fetching content from your first webpage! Now,
let's put your skills to the test. You need to fetch
content from a specific webpage.
"""

import requests

# TODO: Fetch the homepage of a bookstore that contains famous book quotes
url = 'http://quotes.toscrape.com'
response = requests.get(url)

# Check if we successfully got the website's content
if response.ok:
    # TODO: Print a the webpage content
    print("successfully Fetch the homepage of a bookstore that contains famous book quotes")
    print(response.text[:500])
else:
    print("Failed to Fetch the homepage of a bookstore that contains famous book quotes")