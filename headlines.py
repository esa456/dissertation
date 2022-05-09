import urllib.request
from bs4 import BeautifulSoup
import re

##############################################################################################################
# Clean up the logic time permitting
##############################################################################################################
def funScrapeHeadlines(base_url, prefix):
    
    page_top = urllib.request.urlopen(base_url)#for the first page 
    soup1 = BeautifulSoup(page_top, 'html.parser') #parse the html 

    headlinesDict = {}
    counter = 1
    article_headline = soup1.find("div", class_ = 'headline') #top story
    for item in article_headline.find_all("a"):
        iLink = prefix + item['href']
        iHeadline = item.text.strip()
        
        iDict = {'URL' : iLink, 'Headline' : iHeadline}
        
        headlinesDict.update({counter : iDict})
        counter = counter + 1
    
    article_box = soup1.find("table")

    for iTD in article_box.find_all("td"):
        iRawHeadline = re.sub('<[^>]+>', '', str(iTD.find_all("div", class_ = 'headline').copy()))
        iRawHeadline2 = ' '.join(iRawHeadline.split())
        iHeadline = iRawHeadline2.replace('[', '').replace(']', '').strip()
        
        iLink = prefix + iTD.find('a')['href']
        
        iDict = {'URL' : iLink, 'Headline' : iHeadline}
        
        headlinesDict.update({counter : iDict})
        counter = counter + 1
        
    #request page 1 through n
    n = 9                                                                                # number of pages to scrape
    for i in range(1, (int (n)+1)):                                                           # loop over pages 1 to n+1
        page = urllib.request.urlopen (base_url + "?page=%d" % i)                       # read the page
        soup4 = BeautifulSoup(page, 'html.parser')                                      # parse the html on the page
        data = soup4.findAll('div', attrs={'class': 'stories-lineup bigHeader'})        # isolate the div we want
        for div in data:                                                                # loop
            links = div.findAll('a', attrs={'class': ' '})                              # find all 'a' link with 'a' blank class
            k = 0                                                                       # initialise 'a' link count variable
            for a in links:                                                             # loop through the 'a' links
                k += 1                                                                  # increment the headline count 
                #print(a.text)                                                         #output the headline
                
                iLink = prefix + a['href']
                
                iRawHeadline2 = ' '.join(a.text.split())
                iHeadline = iRawHeadline2.replace('[', '').replace(']', '').strip()
                iDict = {'URL' : iLink, 'Headline' : iHeadline}
        
                headlinesDict.update({counter : iDict})
                counter = counter + 1
                
                                                                      
    return headlinesDict   

 
