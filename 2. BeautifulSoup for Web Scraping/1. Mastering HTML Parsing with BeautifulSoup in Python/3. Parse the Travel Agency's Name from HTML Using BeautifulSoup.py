from bs4 import BeautifulSoup

# Let's pretend we have fetched the HTML of a travel agency website page
html_content = '<div><h1>Welcome to Cosmo Travels!</h1><p>Explore the world with us.</p></div>'

# TODO: Create a BeautifulSoup object to parse the HTML content. Use 'html.parser' as the parser
soup = BeautifulSoup(html_content,'html.parser')
# TODO: Use the find method to locate the <h1> tag and store its text in a variable
variable = soup.find('h1').text
# TODO: Print the agency's name
print(variable)