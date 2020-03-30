import requests
from bs4 import BeautifulSoup
import pafy
import pandas as pd
import pickle

def scrap(search_topic):
    url="https://www.youtube.com/results?search_query="+search_topic
    source_code=requests.get(url)
    plain_text=source_code.text
    strip = BeautifulSoup(plain_text)
    list_of_links = ["https://www.youtube.com"+i['href'] for i in strip.findAll('a', {'class':'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link'})]
    return list_of_links

def collect_videos(queries):
     for link in scrap(queries):
               links.append(link)
        
links = []
new_topics = ['satisfying videos', 'pets', 'cats', 'dog grooming', 'artificial intelligence', 'data science', 'how stuff work', 'DIY', 'cooking','python','bts','pewdiepie','asmr','billie eilish','fornite','minecraft','ariana grande','t series','game of throne','coldplay','avengers','karaoke','snl']

collect_videos(new_topics)

file = open('link4.pickle','wb')
pickle.dump(links,file)
file.close()

