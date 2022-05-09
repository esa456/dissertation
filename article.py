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

  
#number of pages
#page_num = soup1.find("div", class_ = "pagination")
#for item in page_num.find_all("a", href=True)[2:]:
#    page = (item['href'])
#    n = ''.join(c for c in page if c in '0123456789')

#top story
article_headline = soup1.find("div", class_ = "headline")
for item in article_headline.find_all("a")[0:]:
    print(item.text)
'''
#article_main = soup1.find("div", class_ = "headline" )#return the time the article was released
#for item in article_main.find_all("time")[0:]:
#    print(item)

#article_box_link = soup1.find("p", class_ = "desc")#this is for the subtext under the headline
#for item in article_box_link.find_all("a")[0:]:
#    print(soup1.find('p').text)


#main stories
article_box = soup1.find("table")
for row in article_box.find_all("tr")[0:]:
    #print (row)
    cells = row.find_all("td")
    cells = row.text.strip()
    print("\n")
    print(cells)
    #print(article_box)
'''
article_box = soup1.find("div", class_ = "filmstrip filmstrip4")
for item in article_box.find_all("tr")[0:]:
        for head in item.find_all("div", class_ = "headline")[0:]: 
            print(head.text)

#request page 1 through n
n = 3                                                                                   # number of pages to scrape
for i in range(1, (int (n)+1)):                                                           # loop over pages 1 to n+1
    page = urllib.request.urlopen (base_url + "?page=%d" % i)                       # read the page
    soup4 = BeautifulSoup(page, 'html.parser')                                      # parse the html on the page
    data = soup4.findAll('div', attrs={'class': 'stories-lineup bigHeader'})        # isolate the div we want
    for div in data:                                                                # loop
        links = div.findAll('a', attrs={'class': ' '})                              # find all a link with a blank class
        k = 0                                                                       # initialise a link count variable
        for a in links:                                                             # loop through the a links
            k += 1                                                                  # increment the link count
            #print ("page " + str(i) + " (" + str(k) + "): " + prefix + a['href'])   # output the link
            print(a.text)    

#if errors occur, check Internet connection




