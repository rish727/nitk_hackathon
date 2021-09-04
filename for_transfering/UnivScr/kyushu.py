import requests
import re
from bs4 import BeautifulSoup

load_url = 'https://www.kyushu-u.ac.jp/ja/topics/' #'https://www.kyushu-u.ac.jp/ja/'
base = 'https://www.kyushu-u.ac.jp'

"""
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
"""

def get(): 
    univ_info = list()
    univ_info_time = list()
    url = list()

    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")

    # for element in soup.find_all(class_="main").find_all(class_="a_new"):  
    #     print(element.text)
        
    body = soup.find_all(class_="txtarea")
    body = body[1]

    #body = soup.select(".txtarea").text
    
    for cell in body.find_all('dl'):
        for info in cell.find_all('a'):  
            univ_info += [info.text]
            #url += [base+ info.get('href')]
        for time in cell.find_all('dt'):  
            univ_info_time += [time.text]
        
        for link in cell.find_all('a'):  
           url += [base+ link.get('href')]
    
    return univ_info, univ_info_time, url
   
if __name__ == "__main__":
    get()
    #print(get())
    
    
    
    
