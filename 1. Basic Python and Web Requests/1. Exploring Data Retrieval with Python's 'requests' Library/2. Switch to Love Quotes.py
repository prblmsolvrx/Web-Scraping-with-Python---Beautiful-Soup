"""
You've done well exploring book-related quotes.
Now, let's shift our focus to love-related quotes.
Modify the URL in your code to fetch love-related
quotes from the same website. Notice how a simple
change to the URL can alter the data we retrieve.
Ready to see the difference?
"""
import requests

# Fetch content from the books section in the quotes website
# TODO: Update the URL to fetch love-related quotes
url = 'http://quotes.toscrape.com/tag/love-related/'
response = requests.get(url)

if response.ok:
    # TODO: Update the message to reflect the change
    print("love-related quotes fetched successfully!")
    print(response.text[:1000])  # Display a snippet from the fetched webpage content