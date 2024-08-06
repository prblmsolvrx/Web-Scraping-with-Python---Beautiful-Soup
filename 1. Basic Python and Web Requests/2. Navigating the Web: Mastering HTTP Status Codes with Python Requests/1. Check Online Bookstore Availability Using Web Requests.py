"""
Have you ever wondered if your favorite Online Bookstore is up and running without having to
check the website manually? The given code does precisely that by making a web request
to http://quotes.toscrape.com and then checks if the bookstore page is available.
Run the code to witness the magic of web requests in action!
"""

import requests

# Simulate checking the availability of the online bookstore main page
response = requests.get('http://quotes.toscrape.com')

if response.status_code == 200:
    print("The Online Bookstore is available!")
elif response.status_code == 404:
    print("The Online Bookstore page was not found!")
else:
    print("Something went wrong with the Online Bookstore page.")