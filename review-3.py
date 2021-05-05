from bs4 import BeautifulSoup
import urllib.request
from re import sub

wiki_link = "https://en.wikipedia.org/wiki/Quadtree"
wiki_page = urllib.request.urlopen(wiki_link)
wiki_soup = BeautifulSoup(wiki_page, 'html.parser')
wiki_soup.prettify()
title = wiki_soup.find(id="firstHeading")
print(title.string)


wiki_content=wiki_soup.find_all(id="mw-content-text")
wiki_desc_raw = wiki_soup.find_all('p')
wiki_desc = [comment.text for comment in wiki_desc_raw]
print(wiki_desc[0])

gfg_link = "https://www.geeksforgeeks.org/quad-tree/"
gfg_page = urllib.request.urlopen(gfg_link)
gfg_soup = BeautifulSoup(gfg_page, 'lxml')
gfg_div_text = gfg_soup.find_all("div", attrs={'class': 'text'})
gfg_desc_raw = gfg_soup.find_all('p')
gfg_desc = [comment.text for comment in gfg_desc_raw]

print(gfg_desc[0])  # gfg description

gfg_steps_raw = gfg_soup.find_all('ol')
gfg_steps = [comment.text for comment in gfg_steps_raw]
print(gfg_steps[0])  # steps to construct a quadtree

print(gfg_desc[2])  # insert function

print(gfg_desc[3])  # search function
