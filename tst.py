import urllib.request
from bs4 import BeautifulSoup
import os, sys, csv

#specify url
base_url = 'http://money.cnn.com/data/dow30/'

page = urllib.request.urlopen (base_url)

#parse the html
soup1 = BeautifulSoup(page, 'html.parser')


#main stories
article_box = soup1.find("div", class_ = "mod-dow30info")
for row in article_box.find_all("tr")[2:]:
    for cells in row.find_all("td", class_ = "wsod_firstCol"):
        #cells = row.text.strip()
        #print("\n")
        print(cells.text)



            
                

    
            



