import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
# Updated URL to point to the site with images
url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img')

os.makedirs('images', exist_ok=True)

for image in images:
    # TODO: Extract the URL of the image from the 'src' attribute
    img_src = image.get('src')
    img_url = urljoin(url, img_src)
    
    # TODO: Download the image using requests module. For simplicity, you can use url + src to get the full image URL.
    img_response = requests.get(img_url, stream=True)
    
    img_src = os.path.basename(img_src)
    with open(f"images/{img_src}", 'wb') as f:
        for chunk in img_response.iter_content(1024):
            f.write(chunk)
    print(f"Saved {img_src}")
