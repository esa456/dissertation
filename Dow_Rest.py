import urllib.request
from bs4 import BeautifulSoup
import os, sys, csv

def funScrapeDowData(dow_url):
    page = urllib.request.urlopen (base_url)
    soup1 = BeautifulSoup(page, 'html.parser')
    dow_url                         = 'https://www.cnbc.com/dow-components/'
    
        
    article_box = soup1.find("div", class_ = "unit col1")
    for row in article_box.find_all("tr")[0:]:
        for cells in row.find_all("td", class_ = "first text"):
            print(cells.text)
        
            
           
                    
            
                
