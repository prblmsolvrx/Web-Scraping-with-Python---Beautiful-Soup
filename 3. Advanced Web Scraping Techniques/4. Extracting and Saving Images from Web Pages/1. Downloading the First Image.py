"""
Great job so far! Now let's run the code you saw in the lesson.
In this exercise, we will download the first image from the website and save it locally.
Here's a brief recap of the key steps:
First, we fetch the webpage content using a GET request and parse it with BeautifulSoup.
Next, we find all the image tags in the HTML content and extract the URL of the first image.
Finally, we download the image and save it to the images directory.
Run the code below to see it in action and observe how the image is saved in the images directory.
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
src = images[0]['src']
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