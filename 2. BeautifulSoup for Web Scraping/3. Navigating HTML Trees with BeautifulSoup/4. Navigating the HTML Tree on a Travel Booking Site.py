from bs4 import BeautifulSoup

# Mock HTML snippet of a travel booking website
html_content = """
<div id='destination'>
    <h1>Paris</h1>
    <ul class='offers'>
        <li class='package'>Eiffel Tower Tour</li>
        <li class='package'>Louvre Museum Pass</li>
        <li class='package'>Seine River Cruise</li>
    </ul>
</div>
"""

soup = BeautifulSoup(html_content, 'html.parser')
offers_list = soup.find('ul', class_='offers')
print("Parent of <ul> element:", offers_list.parent.name)

# TODO: Using the offers_list, iterate through its children to print the text of each 'li' element.
for li in offers_list.find_all('li'):
    print(li.text)


    
    
    
