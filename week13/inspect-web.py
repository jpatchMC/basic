#!/usr/bin/env python3

import requests,bs4

res = requests.get('https://notpurple.com')
res.raise_for_status()

myHTML = bs4.BeautifulSoup(res.text,features="html.parser")

#print(type(myHTML))
#print(type(myHTML.title))
print(myHTML.title)
print(myHTML.title.text)
links = myHTML.select('a')
#print(type(links))
print(links)
print(f"Number of links {len(links)}")
#print((images[0]['src']))