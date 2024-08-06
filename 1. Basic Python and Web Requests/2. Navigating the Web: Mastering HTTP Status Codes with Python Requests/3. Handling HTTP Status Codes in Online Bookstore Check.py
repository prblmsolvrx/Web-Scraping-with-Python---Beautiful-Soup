"""
let's practice handling a different outcome from our online bookstore.
Imagine you want to check if a specific resource exists and, depending
on the response, take appropriate action. Create the conditional
logic based on the HTTP status code returned when making a GET request.
"""

import requests

# Check the status code of the online bookstore home page
response = requests.get('http://quotes.toscrape.com')
if response.status_code == 200:
    print("Online Bookstore is up and running!")
elif response.status_code == 404: # TODO: Determine if the resource doesn't exist
    print("Online Bookstore page not found.")
else:
    print("There was a problem accessing the Online Bookstore.")