import requests
from bs4 import BeautifulSoup

url = 'https://app.isokko.com'
response = requests.get(url)

html_content = response.text
soup = BeautifulSoup(html_content,'html.parser')
print(soup.prettify())