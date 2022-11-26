#!/usr/bin/env python3

import requests,bs4

res = requests.get('http://www.coolthings.com')
res.raise_for_status()

myHTML = bs4.BeautifulSoup(res.text,features="html.parser")

print(type(myHTML))
print(type(myHTML.title))
print(myHTML.title)
print(myHTML.title.text)
images = myHTML.select('img')
print(type(images))
print((images[0]['src']))