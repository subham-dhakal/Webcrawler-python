#Crawls the tech site of Nepal to get the relevant data


import requests
from bs4 import BeautifulSoup

def Download(max_size):
    page=1
    while(page<=max_size):
        url="https://www.gadgetbytenepal.com/blog-news-list/page/"+str(page)
        Source_code=requests.get(url)
        Plain_text=Source_code.text
        soup=BeautifulSoup(Plain_text,"lxml")
        for links in soup.findAll('a',{'rel':'bookmark'}):
            title=links.get('title')
            href=links.get('href')
            print(title)
            print(href)
            print()
        page+=1
        print("-----------------------------------------------------")

Download(3)
