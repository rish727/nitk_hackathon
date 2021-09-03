import requests
import re
from bs4 import BeautifulSoup

load_url = 'https://www.kyushu-u.ac.jp/ja/'


def get(): 
    univ_info = list()
    univ_info_time = list()

    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")

    # for element in soup.find_all(class_="main").find_all(class_="a_new"):  
    #     print(element.text)
        
    news_block = soup.find(id="news_block")

    for main in news_block.find_all(class_="main"):
        for h3 in main.find_all("h3"):  
            univ_info += [h3.text]
        for time in main.find_all("time"):  
            univ_info_time += [time.text]
            
    return univ_info, univ_info_time 
        
if __name__ == "__main__":
    get()
    
    
    
    
