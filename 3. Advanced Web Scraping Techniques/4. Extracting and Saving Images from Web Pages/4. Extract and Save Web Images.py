# TODO: Fetch the webpage content using requests.get() and store in `response`
# TODO: Parse the HTML content using BeautifulSoup
# TODO: Find the first image in the HTML using BeautifulSoup
# TODO: Extract the `src` attribute from the first image element
# TODO: Construct the full image URL if it's not complete. Hint - it should look like this: 'https://books.toscrape.com/<src>'
# TODO: Make a GET request to the image URL to download the image
# TODO: Write the image data to a file in a folder named 'images'

import requests
from bs4 import BeautifulSoup
import os

# Updated URL to point to the site with images
url = 'https://books.toscrape.com/'

# Create directory to store images if it doesn't already exist
os.makedirs('images', exist_ok=True)

# Fetch the webpage content using requests.get()
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the first image in the HTML
first_image = soup.find('img')

if first_image:
    # Extract the `src` attribute from the first image element
    src = first_image.get('src')
    
    # Construct the full image URL if it's not complete
    image_url = requests.compat.urljoin(url, src)

    # Make a GET request to the image URL to download the image
    image_response = requests.get(image_url)
    
    # Check if the request was successful
    if image_response.status_code == 200:
        # Write the image data to a file in the 'images' folder
        image_path = os.path.join('images', 'first_image.jpg')
        with open(image_path, 'wb') as file:
            file.write(image_response.content)
        print(f'Image downloaded and saved to {image_path}')
    else:
        print('Failed to download the image.')
else:
    print('No image found on the page.')
