"""
Currently, the code is making a request to a URL and waiting
for a response. The response takes too long, slowing down
the code execution. We need to fix this issue by setting a
timeout for the request for 2 seconds.
"""

import requests

url = "https://postman-echo.com/delay/10"

try:
    response = requests.get(url, timeout = 2)
    print(response.text)
except requests.Timeout: qw34g