
from requests import get
from bs4 import BeautifulSoup
import requests
import time
import os


link = 'http://truyentranhtuan.com/luyen-nguc-trong-sinh-chuong-140/'

page = requests.get(link)
print(link)

soup = BeautifulSoup(page.content, 'html.parser')

viewer = soup.find('div', {'id':'viewer'})

print(viewer)
imgs = soup.find_all('img')

print(imgs  )
