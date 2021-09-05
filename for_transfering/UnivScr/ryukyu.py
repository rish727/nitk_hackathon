import requests
import re
from bs4 import BeautifulSoup

#load_url = 'https://www.kumamoto-u.ac.jp/' #this is hp
load_url = 'https://www.u-ryukyu.ac.jp/news/'

def get(): 
    univ_info = list()
    univ_info_time = list()
    url = list()

    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    
    #tab = soup.find(class_="c-tab__body") #HP
    
    sakana = soup.find(class_="container") #new
    
    for body in sakana.find_all(class_="col-md-6 col-lg-4 mb-5"):
        for cell in body.find_all(class_="card-body bg-gray-100"):
            for info in cell.find_all(class_="font-size-15 font-weight-bold mb-0"):
                univ_info += [info.text]
            
            for time in cell.find_all(class_="font-size-13"):  
                univ_info_time += [time.text]
        
        for link in body.find_all('a'):
            url += [link.get('href')]
            
    return univ_info, univ_info_time, url
        
if __name__ == "__main__":
    get()
    #print(get()) #for demo
    
    
    
    
