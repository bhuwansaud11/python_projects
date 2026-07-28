#Python Web Scraper
import requests
from bs4 import BeautifulSoup

for page in range(1,11):

    url = f"https://quotes.toscrape.com/page/{page}"
    response = requests.get(url)
    if response.status_code == 200:
        response = response.text
        soup = BeautifulSoup(response,'lxml')
        quotes = soup.find_all('div',class_='quote')
        for quote in quotes:
            quote_text = quote.find('span',class_='text').text
            author = quote.find('small',class_='author').text
            more_info = quote.find('a')['href']

            print("--Quote--")
            print(f"Quote: {quote_text}")
            print(f"Author: {author}")
            print(f"More about {author}: {'https://quotes.toscrape.com'+more_info}")
            print()
    else:
        print("Failed to retrieve data")
