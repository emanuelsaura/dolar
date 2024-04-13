from bs4 import BeautifulSoup
import requests

website = 'https://www.bna.com.ar/Personas'
result = requests.get(website)

content = result.text
soup = BeautifulSoup(content, 'lxml')

#print(soup.prettify())

box = soup.find('table', class_='cotizacion')
print(box)
