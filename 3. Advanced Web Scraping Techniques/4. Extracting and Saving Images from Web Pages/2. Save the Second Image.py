"""
Great progress so far! Let's make a slight
change to the script so that instead of saving
the first image, we save the second image.
This change will help you understand how
to navigate different elements in the list of images.
Modify the code to save the second image found
on the page instead of the first one.
"""

import requests
from bs4 import BeautifulSoup
import os

# Updated URL to point to the site with images
url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img')

# Let's save the first image to the 'images' directory
# First let's create 'images' directory to save the image
os.makedirs('images', exist_ok=True)

# Get the image source from the src attribute and construct the full URL
src = images[1]['src']
full_src = f"https://books.toscrape.com/{src}" if not src.startswith('http') else src

# Send a GET request to the image URL
img_response = requests.get(full_src, stream=True)

# Save the image to the 'images' directory if the request is successful
if img_response.status_code == 200:
    img_name = os.path.basename(src)
    with open(f"images/{img_name}", 'wb') as f:
        for chunk in img_response.iter_content(1024):
            f.write(chunk)
    print(f"Saved {img_name}")