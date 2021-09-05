import requests
import re
from bs4 import BeautifulSoup

#load_url = 'https://www.kumamoto-u.ac.jp/' #this is hp
load_url = 'https://www.hokudai.ac.jp/news/news/'


def get(): 
    univ_info = list()
    univ_info_time = list()
    url = list()

    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    
    #tab = soup.find(class_="c-tab__body") #HP
    body = soup.find(class_="showall") #new

    for cell in body.find_all('dd'):
        for info in cell.find_all('a'):
            univ_info += [info.text]
            url += [info.get('href')]
    for time in body.find_all('dt'):  
        univ_info_time += [time.text]
            
    return univ_info, univ_info_time, url
        
if __name__ == "__main__":
    get()
    #print(get()) #for demo
    
    
    
    
