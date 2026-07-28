#Python Web Scraper
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com'
response = requests.get(url)
if response.status_code == 200:
    response = response.text
    soup = BeautifulSoup(response,'lxml')
    quotes = soup.find_all('div',class_='quote')
    for quote in quotes:
        quote_text = quote.find('span',class_='text').text
        author = quote.find('small',class_='author').text

        print("--Quote--")
        print(f"Quote: {quote_text}")
        print(f"Author: {author}")
        print()
else:
    print("Failed to retrieve data")
