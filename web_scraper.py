#Python Web Scraper
import requests
from bs4 import BeautifulSoup

print("Type the name of the author you want the quote of")
known_author = input('<')
print('Filtering...')
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
            tags = quote.find('div',class_='tags')
            link_tags = tags.find_all('a')
            tags_text = []
            for link_tag in link_tags:
                tag = link_tag.text
                tags_text.append(tag)
            tags_text = ', '.join(tags_text)
            if known_author.lower()==author.lower():
                print("--Quote--")
                print(f"Quote: {quote_text}")
                print(f"Author: {author}")
                print(f"More about {author}: {'https://quotes.toscrape.com'+more_info}")
                print(f"Tags: {tags_text}")
                print()
    else:
        print("Failed to retrieve data")
