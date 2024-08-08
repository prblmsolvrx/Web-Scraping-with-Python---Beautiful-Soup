from bs4 import BeautifulSoup

# Sample HTML content from a travel booking website
html_content = """
<html>
  <body>
    <div class="flights">
      <h1>Flight Options</h1>
      <ul>
        <li class="flight" id="flight1">Flight 101 to Rome - $499</li>
        <li class="flight" id="flight2">Flight 202 to Paris - $599</li>
      </ul>
    </div>
    <div class="hotels">
      <h2>Hotel Listings</h2>
      <ul>
        <li class="hotel" id="hotel1">Hotel Plaza - $99 per night</li>
        <li class="hotel" id="hotel2">Grand Hotel - $199 per night</li>
      </ul>
    </div>
    <div class="reviews">
      <h3>Customer Reviews</h3>
      <p id="review1">Great experience on Flight 101!</p>
      <p id="review2">Highly recommend Hotel Plaza for the price.</p>
    </div>
  </body>
</html>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Locate the flights div and then find the first flight option within it
flights_div = soup.find('div', class_='flights')
first_flight = flights_div.find('li', class_='flight').text
print(f"First flight option: {first_flight}")

# Navigate to the sibling element of the flights div, i.e., the hotels div, and find the first hotel option
hotels_div = flights_div.find_next_sibling('div', class_='hotels')
first_hotel = hotels_div.find('li', class_='hotel').text
print(f"First hotel option: {first_hotel}")