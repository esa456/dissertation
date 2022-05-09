# This Python file uses the following encoding: utf-8
import urllib.request
from bs4 import BeautifulSoup
import os, sys, csv

#specify url
base_url = 'https://www.cnbc.com/earnings/'
prefix = 'https://www.cnbc.com'

#handle first page
page_top = urllib.request.urlopen (base_url)#for the first page 

#parse the html
soup1 = BeautifulSoup(page_top, 'html.parser') 

article_box = soup1.findAll('div', attrs={'class' : 'filmstrip filmstrip4'})
for div in article_box: 
    headlines = div.findAll('a', attrs={'class': ' '})                              # find all 'a' link with 'a' blank class
    k = 0                                                                       # initialise 'a' link count variable
    for a in headlines:                                                             # loop through the 'a' links
        k += 1                                                                  # increment the headline count 
        print(a.text)                                                         #output the headline
        #headlines.update({counter : a.text})
        #counter = counter + 1

