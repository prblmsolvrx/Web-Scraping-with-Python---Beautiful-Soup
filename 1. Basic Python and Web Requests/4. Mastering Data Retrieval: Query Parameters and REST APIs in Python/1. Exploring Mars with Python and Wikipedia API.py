import requests

# Making a get request to Wikipedia's action API for space exploration topic 'Mars'
params_mars_info = {'action': 'query', 'prop': 'info', 'titles': 'Mars', 'format': 'json'}
response_mars_info = requests.get('https://en.wikipedia.org/w/api.php', params=params_mars_info)

# Check if the request was successful and if so, print a summary
if response_mars_info.ok:
    print(response_mars_info.json()['query']['pages'])

"""
output:
{'14640471': {'pageid': 14640471, 'ns': 0, 'title': 'Mars', 'contentmodel': 'wikitext', 'pagelanguage': 'en', 'pagelanguagehtmlcode': 'en', 'pagelanguagedir': 'ltr', 'touched': '2024-08-05T23:07:10Z', 'lastrevid': 1238837210, 'length': 208978}}
"""