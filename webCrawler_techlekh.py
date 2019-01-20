import requests
from bs4 import BeautifulSoup

def webCrawler(max_pages):
    page=1
    while page<=max_pages:
        url='https://techlekh.com/category/gadgets/page/'+str(page)
        sourceCode=requests.get(url)
        plainText=sourceCode.text
        soup = BeautifulSoup(plainText, "lxml")
        for links in soup.findAll('a',{'rel': 'bookmark'}):
            title=links.string
            href=links.get('href')
            print(title)
            print(href)
            print()
        page += 1
        print("------------------------------------------")


webCrawler(3)
