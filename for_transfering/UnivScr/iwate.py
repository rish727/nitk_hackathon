import requests
import re
from bs4 import BeautifulSoup

#load_url = 'https://www.kumamoto-u.ac.jp/' #this is hp
load_url = 'https://www.iwate-u.ac.jp/info/2021/index.html'
base = 'https://www.iwate-u.ac.jp/info/'

def get(): 
    univ_info = list()
    univ_info_time = list()
    url = list()

    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    
    #tab = soup.find(class_="c-tab__body") #HP
    body = soup.find(class_="contents") #new

    for today in body.find_all(class_="mod-newsList"):
        for cell in today.find_all(class_="table-news"):
            for info in cell.find_all(class_="txt-newsTitle"):  
                univ_info += [info.text]
            for time in cell.find_all(class_="txt-date"):  
                univ_info_time += [time.text]
            for link in cell.find_all('a'):
                s = link.get('href')
                s.replace('/../','')
                url += [base + s.replace('..','')]
            
    return univ_info, univ_info_time, url
        
if __name__ == "__main__":
    print(get())
    #print(get()) #for demo
    
    
    
    
