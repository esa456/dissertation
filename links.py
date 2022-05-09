# This Python file uses the following encoding: utf-8
import urllib.request
from bs4 import BeautifulSoup
import os, sys, csv


#specify url
base_url = 'https://www.cnbc.com/earnings/'
prefix = 'https://www.cnbc.com'
def funScrape(base_url, prefix):
    page = urllib.request.urlopen (base_url)
    #
    #parse the html
    soup1 = BeautifulSoup(page, 'html.parser')
    
    #number of pages
    #page_num = soup1.find("div", class_ = "pagination")
    #for item in page_num.find_all("a", href=True)[2:]:
    #    page = (item['href'])
    #    n = ''.join(c for c in page if c in '0123456789')
    
    #
    #
    # n = 2
    # for i in range(int(n) + 1):
    #     page_rest = urllib.request.urlopen (base_url + "?page=%d" % i)#for the rest of the pages
    #     soup4 = BeautifulSoup(page_rest, 'html.parser')
    #
    #     other stories on page 1 and above
    #     article_list = soup4.find("div", class_ = "stories-lineup bigHeader")
    #     for item in article_list.find_all("li")[0:]:
    #         for head in item.find_all("div", class_ = "headline"):
    #             for link in head.find_all("a", href=True):
    #                 i = set(link)
    #                 for x in i:
    #                     print(prefix + link['href'])
    
    
    headlines = {}
    counter = 1
    article_main_link = soup1.find("div", class_ = "headline")
    for a in article_main_link.find_all("a", href=True)[0:]:
        print(prefix + a['href'])
        headlines.update({counter : prefix + a['href']})
        counter = counter + 1
    
    #main stories links
    article_box_links = soup1.find("table")
    for row in article_box_links.find_all("tr")[0:]:
        for head in row.find_all("div", class_ = "headline"):
            for a in head.find_all("a", href=True):
                print(prefix + a['href'])
                headlines.update({counter : prefix + a['href']})
                counter = counter + 1
'''    
    return headlines

thisHeadlines = funScrape(base_url, prefix)

for iKey in thisHeadlines.keys():
    print(str(iKey) +  thisHeadlines[iKey])
'''

    n = 2                                                                                   # number of pages to scrape
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
                print(prefix + a['href'])
                headlines.update({counter : prefix + a['href']})
                counter = counter + 1
            
    return headlines

thisHeadlines = funScrape(base_url, prefix)

for iKey in thisHeadlines.keys():
    print(str(iKey) +  thisHeadlines[iKey])

'''        

import mysql.connector

cnx = mysql.connector.connect(user='root',password='Jumeirah198', database='articles')
cursor = cnx.cursor()

query = ('INSERT INTO articles (Link) VALUES (NOW(), LOAD_FILE('/Users/Student/Desktop/Computer_science/Year_3/G53IDS/Dissertation/src/links.txt'));',list)

cursor.execute(query) 

cnx.close()
'''
