import mysql.connector
cnx = mysql.connector.connect(user='root', password='tibbtp24',
                              host='127.0.0.1',
                              database='simulator')
cursor = cnx.cursor()
mysql = "select * from candidates"
cursor.execute(mysql)
data = cursor.fetchall()
print (data)
print ("yomama")

