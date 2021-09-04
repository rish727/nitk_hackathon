import requests
import re
from bs4 import BeautifulSoup

#load_url = 'https://www.kumamoto-u.ac.jp/' #this is hp
load_url = 'http://www.miyazaki-u.ac.jp/newsrelease/'
base = 'http://www.miyazaki-u.ac.jp/'

def get(): 
    univ_info = list()
    univ_info_time = list()
    url = list()

    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    
    #tab = soup.find(class_="c-tab__body") #HP
    body = soup.find(id="newsList") #new
    

    for cell in body.find_all(class_="newsBox"):
        for info in cell.find_all(class_="desc"):
            univ_info += [info.text]
        for time in cell.find_all(class_="date"):  
            univ_info_time += [time.text]

        if not (base in str(cell.get('href'))):
            url += [base + cell.get('href')]
        else:
            url += [ cell.get('href')]

    return univ_info, univ_info_time, url
        
if __name__ == "__main__":
    print(get())
    #print(get()) #for demo
    
    
    
    
