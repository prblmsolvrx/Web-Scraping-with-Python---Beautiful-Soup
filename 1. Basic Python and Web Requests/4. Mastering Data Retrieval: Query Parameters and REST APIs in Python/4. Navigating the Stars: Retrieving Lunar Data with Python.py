"""
As you've journeyed through the digital cosmos,
collecting data with Python, the time has arrived
to direct your exploratory efforts closer to home.
Harness the power of web requests to gather information
about the Earth, our blue and green spaceship, from Wikipedia.
Dive into the functionalities of Python's requests
library to interact with Wikipedia's REST API.
Prepare for a descent into the atmosphere of API
requests and data retrieval. Fasten your seatbelts
for this enlightening voyage to gather knowledge about our planet!
"""

import requests

# TODO: Define a variable named `url_wiki_earth` that stores the URL to access information about the Earth from Wikipedia's REST API: 'https://en.wikipedia.org/api/rest_v1/page/title/Earth' 
url_wiki_earth = 'https://en.wikipedia.org/api/rest_v1/page/title/Earth'
# TODO: Use the `requests.get()` method to send a GET request to the Wikipedia REST API using the `url_wiki_earth`.
response = requests.get(url_wiki_earth)
# TODO: Print the JSON response if the request is successful. Otherwise, print an error message indicating the failure to fetch data about the Earth.

if response.status_code == 200:
    print(response.json())
else:
    print("failed to fetch")