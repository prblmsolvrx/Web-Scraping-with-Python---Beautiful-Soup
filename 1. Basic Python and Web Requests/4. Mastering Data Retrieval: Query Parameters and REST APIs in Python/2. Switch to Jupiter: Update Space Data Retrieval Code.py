"""
In your space exploration journey through the vast universe of coding,
let's shift our gaze from Mars to another majestic giant, Jupiter.
Use your newfound knowledge of query parameters to update the existing code,
so it fetches information about Jupiter from Wikipedia's API instead of Mars.
How do the details you retrieve change?
"""

import requests

# Fetching data about Mars using query parameters and REST API
url = 'https://en.wikipedia.org/w/api.php'
# TODO: Update the code to fetch details about Jupiter instead
params = {
    'action': 'query',
    'prop': 'info',
    'titles': 'Jupiter',
    'format': 'json'
}
response = requests.get(url, params=params)

if response.ok:
    print(response.json()['query']['pages'])  # Prints information about Mars page

"""
output:
{'38930': {'pageid': 38930, 'ns': 0, 'title': 'Jupiter', 'contentmodel': 'wikitext',
'pagelanguage': 'en', 'pagelanguagehtmlcode': 'en', 'pagelanguagedir': 'ltr',
'touched': '2024-08-06T04:34:07Z', 'lastrevid': 1238877278, 'length': 182351}}
"""