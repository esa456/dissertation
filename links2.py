import urllib.request

from bs4 import BeautifulSoup

import os, sys, csv


def funScrapeLinks(base_url, prefix):

    page = urllib.request.urlopen (base_url, prefix)
    soup1 = BeautifulSoup(page, 'html.parser')
    
    #number of pages
    #page_num = soup1.find("div", class_ = "pagination")
    #for item in page_num.find_all("a", href=True)[2:]:
    #    page = (item['href'])
    #    n = ''.join(c for c in page if c in '0123456789')

    URLs = {}
    counter = 1
    article_main_link = soup1.find("div", class_ = "headline") #top story
    for a in article_main_link.find_all("a", href=True)[0:]:
#        print(prefix + a['href'])
        URLs.update({counter : prefix + a['href']})
        counter = counter + 1

    #main stories links
    article_box_links = soup1.find("table")

    for row in article_box_links.find_all("tr")[0:]:
        for head in row.find_all("div", class_ = "headline"):
            for a in head.find_all("a", href=True):
                #print(prefix + a['href'])
                URLs.update({counter : prefix + a['href']})
                counter = counter + 1
    
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
                #print(prefix + a['href'])
                URLs.update({counter : prefix + a['href']})
                counter = counter + 1
    
    return URLs

#########################################################################################################################

def funAnalyse(URLsDict):
    analysisDict = {'output' : 'MyOutput', 'output2' : 'MyOutput2'}
    return analysisDict

def funClassifyAll(URLsDict):
    classDict = {}
    for iKey in URLsDict.keys():
        iURL = URLsDict[iKey]
        
        outTuple = ('positive', 0.95)
        classDict.update({iURL : outTuple})
        
    
    return classDict


def main():
    base_url = 'https://www.cnbc.com/earnings/'
    prefix = 'https://www.cnbc.com'
    
    URLsDict = funScrape(base_url, prefix)
    
    myAnalysisDict = funAnalyse(URLsDict)
    classificationDictionary = funClassifyAll(URLsDict)
    
    
    for iKey in myAnalysisDict.keys():
        print(myAnalysisDict[iKey])
    return

#########################################################################################################################
os.chdir(os.path.dirname(os.path.realpath('__file__')))

if __name__ == "__main__":
    print('Printing indices...')
    try:
        main()
#        input("Press Enter to continue...")
    except:
        print('Something is wrong')
        input("Press Enter to continue...")
    finally:
        print('All done')
        input("Press Enter to continue...")
            