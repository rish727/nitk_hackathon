import requests
import re
from bs4 import BeautifulSoup

# Webページを取得して解析する
kyushu = 'https://www.kyushu-u.ac.jp/ja/'

load_url = kyushu
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# for element in soup.find_all(class_="main").find_all(class_="a_new"):  
#     print(element.text)
    
news_block = soup.find(id="news_block")

for main in news_block.find_all(class_="main"):
    for a_new in main.find_all("h3"):  
        print(a_new.text)
    for a_new in main.find_all("time"):  
        print(a_new.text)
        
