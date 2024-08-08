from bs4 import BeautifulSoup

# Simplified HTML content from a travel agency website
html_content = '<div><h1>Welcome to the Amazing Travel Agency!</h1><p>Plan your next adventure with us.</p></div>'
soup = BeautifulSoup(html_content, 'html.parser')

# Find the heading (h1) of the Travel Agency website
heading = soup.find('h1').text
print(f"Travel Agency Heading: {heading}")

# Output
# Travel Agency Heading: Welcome to the Amazing Travel Agency!
