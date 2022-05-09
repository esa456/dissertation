import urllib.request
from bs4 import BeautifulSoup

def openLink(url):
    

    page                    = urllib.request.urlopen(url) 
    soup                    = BeautifulSoup(page, 'html.parser') 
    individual_article_text = soup.find("div", class_ = "unit col1")
    artText                 = individual_article_text.text.strip()
    
            
    return artText


        
    
