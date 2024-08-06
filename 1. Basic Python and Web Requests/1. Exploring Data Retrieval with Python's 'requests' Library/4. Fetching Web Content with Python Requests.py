"""
Great job reaching this point, Space Explorer! Now,
for your final challenge in this lesson,
let's craft a script that fetches data from the web.
Use the requests library to retrieve the first 500 characters
of a webpage's content from http://quotes.toscrape.com. Remember,
checking if your request was successful is crucial before attempting to print anything!
"""

import requests

# TODO: Use the requests library to fetch the content of the webpage (http://quotes.toscrape.com)
url = "http://quotes.toscrape.com"
response = requests.get(url)
# TODO: Check if the request was successful
if response.ok:
    print("successfull")
    print(response.text[:500])
# TODO: If successful, print the first 500 characters of the webpage's content
else:
    print("failed")