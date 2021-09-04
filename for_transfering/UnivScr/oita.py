import requests
import re
from bs4 import BeautifulSoup

#load_url = 'https://www.kumamoto-u.ac.jp/' #this is hp
load_url = 'https://www.oita-u.ac.jp/'

def get(): 
    univ_info = list()
    univ_info_time = list()
    url = list()

    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    
    #tab = soup.find(class_="c-tab__body") #HP
    body = soup.find(class_="info") #new
    

    for cell in body.find_all('dl'):
        for info in cell.find_all('a'):
                univ_info += [info.text]
        for time in cell.find_all('dt'):  
            univ_info_time += [time.text]
        for link in cell.find_all('a'):
            url += [load_url + link.get('href')]
            
    return univ_info, univ_info_time, url
        
if __name__ == "__main__":
    print(get())
    #print(get()) #for demo
    
    
    
    
