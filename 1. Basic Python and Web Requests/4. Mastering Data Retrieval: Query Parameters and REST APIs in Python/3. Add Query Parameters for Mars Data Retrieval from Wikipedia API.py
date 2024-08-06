"""
Great job exploring data from Wikipedia! Now, let's dive a little deeper into space exploration.
You have information about Mars ready to retrieve using the Wikipedia action API. 
Your task is to implement the missing query parameters and the request line to fetch data about Mars.
Consider which parameters you should include to obtain information on Mars and how to craft the request.
"""

import requests

# TODO: Define the query parameters for requesting information about Mars from Wikipedia's action API
params_mars_info = {
    # TODO: Specify the action to 'query', prop to 'info', titles to 'Mars', and format for the query in 'json'
    'action':'query', 
    'prop':'info',
    'titles':'Mars',
    'format':'json'
}

# TODO: Make the request to the Wikipedia action API 'https://en.wikipedia.org/w/api.php' with the defined params_mars_info
response_mars = requests.get('https://en.wikipedia.org/w/api.php', params=params_mars_info)# Fill in with request code

# Check request status and print the title of the page from the response if successful
if response_mars.ok:
    pages = response_mars.json()['query']['pages']
    for page_id in pages:
        print(pages[page_id]['title'])

"""
output : Mars
"""