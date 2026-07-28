#Python Web Scraper
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup()
if response.status_code == 200:
    response = response.text
    soup = BeautifulSoup(response,'lxml')
    quotes = soup.find_all('div',class_='quote')
    for quote in quotes:
        print(quote.text)
else:
    print("Failed to retrieve data")
