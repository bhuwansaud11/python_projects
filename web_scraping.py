
import requests
from bs4 import BeautifulSoup

unknown_country = input('Enter the country from where you dont want the car: ')
html_text = requests.get('https://webscraper.io/test-sites/pagination').text
soup = BeautifulSoup(html_text,'lxml')
cars = soup.find_all('div',class_ = 'col-md-4 col-xl-4 col-lg-4')
for car in cars:
    body = car.find('div',class_='card-body')
    link_body = body.find('a') if body else None
    if link_body and 'Mercedes' in link_body.text:
        car_name = link_body.text.strip()
        more_info = link_body['href']
        details = body.find_all('p',class_='card-text')
        for detail in details:
            b_tag = detail.find('b')
            if b_tag and 'Country' in b_tag.text:
                country = b_tag.next_sibling.strip()
                if unknown_country!= country:

                    print(f"Car Name: {car_name}")
                    print(f"Origin: {country}")
                    print(f"More Info: {more_info}")