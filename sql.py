import sys
import mysql.connector as mc
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
'''
cursor.execute("""INSERT INTO `Sys`.`Articles`(`ID`,`URL`,`Headline`,`Classification`,`ClassProb`,`Sentiment`,`SentProb`) 
VALUES
('The fifty fifth thing that could save the tanking markets — earnings season',
'https://www.cnbc.com/2018/04/02/companies-prepare-to-come-to-the-rescue-of-faltering-stock-market.html',
'related',
0.904,
'positive',
0.999);""")
'''


connection.commit()


cursor.close()
connection.close()

 print(headlinesAnalysis[3]) #this code prints the respective dictionaries and their keys

for iKey in headlinesAnalysis:
        print(iKey) #prints the keys that are related
        
for iKey in headlinesAnalysis:
        print (headlinesDict[iKey]['URL']) #prints the urls that are related

for iKey in headlinesAnalysis:
        print (headlinesDict[iKey]) #prints the subdictionaries that are related
        
         subDict = headlinesDict[iKey]

    for iKey in headlinesDict:
        subDict = headlinesAnalysis[iKey]
        print (subDict)















