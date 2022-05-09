import mysql.connector

cnx = mysql.connector.connect(user='root',password='Jumeirah198', database='articles')
cursor = cnx.cursor()

query = ("SELECT * FROM articles.Article")

cursor.execute(query) 
