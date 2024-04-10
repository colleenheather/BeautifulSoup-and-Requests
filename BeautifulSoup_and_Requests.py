from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

print(soup)
print(soup.prettify())

soup.find('div')
# only shows very first div tag in html

soup.find_all('div')

soup.find_all('div', class_ = 'col-md-12')

soup.find('p', class_ = 'lead').text.strip()
# cant use .find_all with .text

soup.find_all('th')

soup.find('th').text.strip()



