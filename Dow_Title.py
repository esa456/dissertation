import urllib.request
from bs4 import BeautifulSoup
import os, sys, csv

def funScrapeDowStock(dow_url):
    page = urllib.request.urlopen (dow_url)
    dow_url                         = 'https://www.cnbc.com/dow-components/'
    soup1 = BeautifulSoup(page, 'html.parser')
    
    DowDict = {}
    counter = 1
    article_box = soup1.find("", class_ = "mod-dow30info")
    for row in article_box.find_all("tr")[2:]:
        for cells in row.find_all("td", class_ = "wsod_firstCol"):
            iTitle = cells.text
            
            iDowDict = {'Title' : iTitle}
            
            DowDict.update({counter : iDowDict})
            counter = counter + 1
    
        
            
'''
            
            for other in row.find_all("td", class_ = "wsod_aRight"):
                iData = other.text
                
                iDataDict = {'Data' : iData}
                
                DowDict.update({iTitle : iDataDict})
    
'''
    
    