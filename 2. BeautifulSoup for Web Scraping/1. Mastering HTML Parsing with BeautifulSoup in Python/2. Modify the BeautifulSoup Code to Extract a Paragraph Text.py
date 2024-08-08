from bs4 import BeautifulSoup

# Simulate an HTML content from a Travel Agency website
html_content = '<div><h1>Welcome to the Best Travel Agency!</h1><p>Explore the world with us.</p></div>'
soup = BeautifulSoup(html_content, 'html.parser')

# TODO: Print the introductory message found in the first paragraph `<p>` tag
intro_message = soup.find('p').text
# TODO: Remember to update the print message to 'Intro Message:' 
print(f"Intro message : {intro_message}") 