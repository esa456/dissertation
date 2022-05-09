from main import headlinesAnalysis
import mysql.connector as mc
#This tells the database to delete everything in the target table
def query():            
    try:
        connection = mc.connect (host = "localhost",
                                         user = "root",
                                         passwd = "Jumeirah198",
                                         db = "Sys")
    except mc.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)
        
    cursor = connection.cursor()
        
    cursor.execute ("DELETE FROM `Sys`.`Articles`")
        
    connection.commit()
                
                
    cursor.close()
    connection.close()    
    
  
#this code prints the queries out exactly how I need them, so they can be copied and pasted into the database 
def printquery():
    for iKey in headlinesAnalysis.keys():
        isubDict = headlinesAnalysis[iKey]
        iHeadline = isubDict['Headline'] 
        iURL = isubDict['URL']
        iClassProb = isubDict['ClassProb']
        iSentiment = isubDict['Sentiment']
        iSentProb = isubDict['SentProb']
        print ("INSERT INTO `Sys`.`Articles`(`Headline`,`URL`,`ClassProb`,`Sentiment`,`SentProb`)VALUES(",('"'+iHeadline+'"' + ','),('"'+iURL+'"'+','),iClassProb,',',('"'+iSentiment+'"'+','),iSentProb, ");")
            