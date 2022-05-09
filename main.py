import urllib.request
import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
import mysql.connector as mc
import sys
from bs4 import BeautifulSoup
   
from query import query
from query import printquery
from headlines import funScrapeHeadlines 
#from links2 import funScrapeLinks


from text_classification import classify
from sentiment_analysis import classify2


from individual import openLink



def main():
    base_url                        = 'https://www.cnbc.com/earnings/'
    prefix                          = 'https://www.cnbc.com'
    # here we first scrape the headlines
    headlinesDict                   = funScrapeHeadlines(base_url, prefix)
    
    # here we classify the headlines
    headlinesAnalysis               = {}
    
    for iKey in headlinesDict.keys():
        
        iHeadline                       = headlinesDict[iKey]['Headline']
        iClassificationResults          = classify(iHeadline)[0]
        iClassification                 = iClassificationResults[0]
        iClassProb                      = iClassificationResults[1]
        
        # if its classified then we open the link and classify the URL
        if iClassification == 'related':            
            iArtText                        = openLink(headlinesDict[iKey]['URL'])
            iArtTextClassification          = classify2(iArtText)[0]
            
            iAnalysisDict = {'URL' : headlinesDict[iKey]['URL'], \
                             'Headline' : iHeadline, \
                             'ClassProb' : iClassProb, \
                             'Sentiment' : iArtTextClassification[0], \
                             'SentProb' : iArtTextClassification[1]}
            
            headlinesAnalysis.update({iKey : iAnalysisDict})

    for iKey in headlinesAnalysis.keys():
        isubDict = headlinesAnalysis[iKey]
        iHeadline = isubDict['Headline'] 
        iURL = isubDict['URL']
        iClassProb = isubDict['ClassProb']
        iSentiment = isubDict['Sentiment']
        iSentProb = isubDict['SentProb']
        print ("INSERT INTO `Sys`.`Articles`(`Headline`,`URL`,`ClassProb`,`Sentiment`,`SentProb`)VALUES(",('"'+iHeadline+'"' + ','),('"'+iURL+'"'+','),iClassProb,',',('"'+iSentiment+'"'+','),iSentProb, ");")
            
   
query()
    


    

