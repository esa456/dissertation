# This Python file uses the following encoding: utf-8
import urllib.request
from bs4 import BeautifulSoup
import os, sys, csv


#specify url
base_url = 'https://www.cnbc.com/earnings/'
prefix = 'https://www.cnbc.com'

page = urllib.request.urlopen (base_url)

#parse the html
soup1 = BeautifulSoup(page, 'html.parser')

#number of pages
page_num = soup1.find("div", class_ = "pagination")
for item in page_num.find_all("a", href=True)[2:]:
    page = (item['href'])
    n = ''.join(c for c in page if c in '0123456789')


article_main_link = soup1.find("div", class_ = "headline")
for item in article_main_link.find_all("a", href=True)[0:]:
    print(prefix + item['href'])

    '''
    page = urllib.request.urlopen (prefix + item['href']) 
    soup2 = BeautifulSoup(page, 'html.parser')

    individual_article = soup2.find("div", class_ = "story-header-left twoCol")
    for item in individual_article.find_all("h1"):
        print(item.text)

    individual_article_text = soup2.find("div", class_ = "unit col1")
    for item in individual_article_text.find_all("article")[0:]:
        print(item.text)
    '''
#main stories links
article_box_links = soup1.find("table")
for row in article_box_links.find_all("tr")[0:]:
    for head in row.find_all("div", class_ = "headline"):
        for url in head.find_all("a", href=True):
            print(prefix + url['href'])
'''
            page = urllib.request.urlopen (prefix + url['href']) 
            soup3 = BeautifulSoup(page, 'html.parser')

            individual_article = soup3.find("div", class_ = "story-header-left twoCol")
            for item in individual_article.find_all("h1"):
                print(item.text)

            individual_article_text = soup3.find("div", class_ = "unit col1")
            for item in individual_article_text.find_all("article")[0:]:
                print(item.text)
        ''' 
#request page 1 through n
for i in range(int(n) + 1):   
    page_rest = urllib.request.urlopen (base_url + "?page=%d" % i)#for the rest of the pages
    soup4 = BeautifulSoup(page_rest, 'html.parser') 
        
    #other stories on page 1 and above   
    article_list = soup4.find("div", class_ = "stories-lineup bigHeader")
    for item in article_list.find_all("li")[0:]:
        for head in item.find_all("div", class_ = "headline"):
            for child in head.find_all("a", class_ = ""):
                for link in child.find_all("a", href=True):
                    print(prefix + link['href'])
                '''
                page = urllib.request.urlopen (prefix + link['href']) 
                soup5 = BeautifulSoup(page, 'html.parser') 
                
                individual_article = soup5.find("div", class_ = "story-header-left twoCol")
                for item in individual_article.find_all("h1"):
                    print(item.text)

                individual_article_text = soup5.find("div", class_ = "unit col1")
                for item in individual_article_text.find_all("article")[0:]:
                    print(item.text)
                    
                    asset cnbcnewsstory imgasset desc_size160_105 card
                    '''

