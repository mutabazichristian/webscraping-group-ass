import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://app.isokko.com/shop?'
response = requests.get(url)

html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

products = soup.find_all(class_='col')
all_products = []

for product in products:
    # Product link
    a = product.find('a', href=True)
    link = a['href'] if a else "No link found"

    # Product name
    h2 = product.find('h2')
    name = h2.text.strip() if h2 else "No name found"

    # Price
    divs = product.select_one('a div div span span')
    price = divs.text.strip() if divs else "No price found"

    # Remove first 4 characters in price (if necessary)
    cleaned_price = price[4:] if price != "No price found" and len(price) > 4 else price

    # Append product details
    all_products.append([name, cleaned_price, link])

# Exclude first two empty products
all_products = all_products[2:]

# Convert to DataFrame
df = pd.DataFrame(all_products, columns=['Product Name', 'Price', 'Product Link'])

# Save to CSV
df.to_csv('scraped_products.csv', index=False)

print("Data saved successfully to 'scraped_products.csv'")
