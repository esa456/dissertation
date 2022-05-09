# This Python file uses the following encoding: utf-8
import urllib.request
from bs4 import BeautifulSoup
import os, sys, csv

#specify url
base_url = 'https://www.cnbc.com/earnings/'
prefix = 'www.cnbc.com'

#handle first page
page = urllib.request.urlopen (base_url) 

#parse the html
soup1 = BeautifulSoup(page, 'html.parser') 


with open('articles_individual.csv', 'r') as csv_f:
    csv_reader = csv.reader(csv_f)   


article_headline = soup1.find("div", class_ = "headline")
for item in article_headline.find_all("a")[0:]:
    print(item.text)

article_box_link = soup1.find("p", class_ = "desc")#this is for the subtext under the headline
for item in article_box_link.find_all("a", href=True)[0:]:
    link = (prefix + item['href'])
    print(link)

article_link = 'link'

page2 = urllib.request.urlopen ('article_link') 
soup3 = BeautifulSoup(article_link, 'html.parser')

#text = soup3.find("div", class_ = "unit col1")
#for item in text.find_all("article")[0:]:
#    print(item.text)
    
'''
#request page 1 through n
n = 1
for i in range(int(n) + 1):   
    page_rest = urllib.request.urlopen (base_url + "?page=%d" % i)#for the rest of the pages
    soup2 = BeautifulSoup(page_rest, 'html.parser') 

    
    #scrape individual article
    individual_article = soup2.find("div", class_ = "story-header-left twoCol")
    for item in individual_article.find_all("h1"):
        print(item.text)

    individual_article_text = soup2.find("div", class_ = "unit col1")
    for item in individual_article_text.find_all("article")[0:]:
        print(item.text)

#no need for table

#with open('article_individual.csv','w') as articles_file:
#    articles_writer = csv.writer(articles_file) 
#    articles_writer.writerow([individual_article, individual_article_text])
'''
