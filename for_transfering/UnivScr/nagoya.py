import requests
import re
from bs4 import BeautifulSoup

#load_url = 'https://www.kumamoto-u.ac.jp/' #this is hp
load_url = 'https://www.nagoya-u.ac.jp/info/index.html#tabs-17'
base = 'https://www.nagoya-u.ac.jp/info/'

def get(): 
    univ_info = list()
    univ_info_time = list()
    url = list()

    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    
    #tab = soup.find(class_="c-tab__body") #HP
    body = soup.find(id="tabs-17") #new

    for cell in body.find_all(class_="info-box clearfix"):
        for info in cell.find_all(class_="title_single"):  
            univ_info += [info.text]
        for time in cell.find_all(class_="day"):  
            univ_info_time += [time.text]
        for link in cell.find_all('a'):
            url += [base + link.get('href')]
            
    return univ_info, univ_info_time, url
        
if __name__ == "__main__":
    print(get())
    #print(get()) #for demo
    
    
    
    
