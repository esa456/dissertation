

def insertquery(dict):
#Creating a sample dictionary of dictionary
    dict = headlinesAnaysis
    yourDict = (headlinesAnalysis)
    yourDict["1"]["URL"] = "https://www.cnbc.com/2018/04/09/how-goldman-sachs-is-playing-the-upcoming-earnings-season-bet-on-stocks-with-real-organic-growth.html"
    yourDict["1"]["Headline"] = "How Goldman is playing earnings season: Get stocks with organic growth"
    
    
    
    yourDict["2"]["ClassProb"] = '0.9978614753023461'
    yourDict["2"]["Sentiment"]= "positive"
    yourDict["2"]["SentProb"]= "0.9998335594332609"
    
    
    # Creating connection to mysql
    conn = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = 'Jumeirah198',
        db = 'Sys'
    )
    
    cursor = conn.cursor()
    
    #Inserting dictionary data into mysql
    for k,v in yourDict.items():
        placeholders = ', '.join(['%s'] * len(yourDict[k]))
        print(placeholders)
        columns = ', '.join(yourDict[k])
        sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('info', columns, placeholders)
        print(sql)
        cursor.execute(sql, list(yourDict[k].values()))
    
    
    conn.commit()
    
    cursor.close()
    conn.close()