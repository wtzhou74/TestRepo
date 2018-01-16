# to connect internet with python
# install package requests first
import requests

# installed beautifulSoup4 Package first
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        # the url you want to crawler
        url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
        # url = 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=watch'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        # find Tag a where class = item-name
        for link in soup.find_all('a', {'class': 'item-name'}):
            href = link.get('href') # get the link
           # title = link.string # the string included in Tag a
            print(href)
           # print(title)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div', {'class': 'i-name'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)

trade_spider(1)
