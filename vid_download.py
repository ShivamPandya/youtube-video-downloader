
# coding: utf-8

# In[43]:


import urllib.request as urlreq
import youtube_dl as ydl
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse

links = []
song_raw = input("Enter song name with singer (Ex: hello by adele): ")
song = song_raw.replace(" ", "")

search = "https://www.youtube.com/results?search_query=" + song
urlparse(search)

#print(search)

x = urlreq.urlopen(search)
soup= bs(x.read(),"html5lib")
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    links.append('https://www.youtube.com' + vid['href'])
ydl.YoutubeDL().download([links[0]])

