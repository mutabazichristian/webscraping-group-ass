import requests
from bs4 import BeautifulSoup

url = 'https://app.isokko.com/shop?'
response = requests.get(url)

html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

products = soup.find_all(class_='col')
all_products = []

"""
class col
    a:href -> product link
    a:div:div:span:span -> Price
    h2 -> product name
"""
for product in products:
    # product link
    a = product.find('a', href=True)
    link = a['href'] if a else "No link found"

    # product name
    h2 = product.find('h2')
    name = h2.text.strip() if h2 else "No name found"

    # price
    divs = product.select_one('a div div span span')
    price = divs.text.strip() if divs else "No price found"

    # remove the first 4 characters in price
    prod = (name, price[4:], link)
    all_products.append(prod)
# 2 of the first products are empty from the site. we can reject those!
all_products = all_products[2:]
print(all_products)

# dump to json or csv
# visualize & analyse
# talk about trends in prices, average price, highest price, longest name lol
