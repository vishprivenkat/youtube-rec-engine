import requests
from bs4 import BeautifulSoup

def scrap(max_pages):
    page=1
    while(page<=max_pages):
        url="https://www.youtube.com/results?search_query=goblin"
        source_code=requests.get(url)
        plain_text=source_code.text
        strip = BeautifulSoup(plain_text)
        links = strip.findAll('h3', {'class':'yt-lockup-title'})
        print(links)
        print("")
        print("")
        print("")
        print("")
        page+=1
scrap(2)
