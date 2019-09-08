import sys
import mysql.connector
import random
import numpy
cnx = mysql.connector.connect(user='simulator', password='mypassword',
                              host='127.0.0.1',
                              database='simulator')
cursor = cnx.cursor()

def getcandidate():
    mysql = "select symbol,mydate,atr from candidates"
    print(mysql)
    cursor.execute(mysql)
    alldata=cursor.fetchall()
    myrow = random.choice(alldata)
    myrisk = 100/myrow[2]*2
    myrisk = int(myrisk)

    return str(myrow[0]),str(myrow[1]),myrisk
def getopenprice(mydate,mysymbol):
    mysql = "select open from stockquotes where symbol = '"+mysymbol+"' and quotedate = '"+mydate+"'"
    print(mysql)
    cursor.execute(mysql)
    openv = cursor.fetchone()
    openv = openv[0]
    return openv
def getcloseprice(mydate,mysymbol):
    mysql = "select close from stockquotes where symbol = '"+mysymbol+"' and quotedate = '"+mydate+"'"
    print(mysql)
    cursor.execute(mysql)
    openv = cursor.fetchone()
    openv = openv[0]
    return openv
def getprofits():
    mysql = "select profit from trades"
    print(mysql)
    cursor.execute(mysql)
    openv = cursor.fetchall()
    profit=[]
    for row in openv:
      #  print (row)
        profit.append(row[0])
    return profit
def getprofitsOutput():
    mysql = "select profit from trades order by entrydate "
    print(mysql)
    cursor.execute(mysql)
    profits = cursor.fetchall()
    return profits
def get250daysbefore(mydate):
    mysql = "select quotedate from stockquotes where symbol = 'SPY' and quotedate <= '"+mydate+"' order by quotedate desc limit 250 "
    print(mysql)
    cursor.execute(mysql)
    newdate = str(cursor.fetchall()[249][0])
    return newdate
def get150daysbefore(mydate):
    mysql = "select quotedate from stockquotes where symbol = 'SPY' and quotedate <= '"+mydate+"' order by quotedate desc limit 150 "
    print(mysql)
    cursor.execute(mysql)
    newdate = str(cursor.fetchall()[149][0])
    return newdate
def get50daysbefore(mydate):
    mysql = "select quotedate from stockquotes where symbol = 'SPY' and quotedate <= '"+mydate+"' order by quotedate desc limit 50 "
    print(mysql)
    cursor.execute(mysql)
    newdate = str(cursor.fetchall()[49][0])
    return newdate
def get30daysbefore(mydate):
    mysql = "select quotedate from stockquotes where symbol = 'SPY' and quotedate <= '"+mydate+"' order by quotedate desc limit 30 "
    print(mysql)
    cursor.execute(mysql)
    newdate = str(cursor.fetchall()[29][0])
    return newdate
def get30daysafter(mydate):
    mysql = "select quotedate from stockquotes where symbol = 'SPY' and quotedate >= '"+mydate+"' order by quotedate limit 30 "
    print(mysql)
    cursor.execute(mysql)
    newdate = str(cursor.fetchall()[29][0])
    return newdate

def get500daysbefore(mydate):
    mysql = "select quotedate from stockquotes where symbol = 'SPY' and quotedate <= '"+mydate+"' order by quotedate desc limit 500 "
    print(mysql)
    cursor.execute(mysql)
    newdate = str(cursor.fetchall()[499][0])
    return newdate
def forward1(mydate):
    mysql = "select quotedate from stockquotes where symbol = 'SPY' and quotedate > '"+mydate+"' order by quotedate limit 1"
    print(mysql)
    cursor.execute(mysql)
    newdate = str(cursor.fetchall()[0][0])
    return newdate
def forward3(mydate):
    mysql = "select quotedate from stockquotes where symbol = 'SPY' and quotedate > '"+mydate+"' order by quotedate limit 3"
    print(mysql)
    cursor.execute(mysql)
    newdate = str(cursor.fetchall()[2][0])
    return newdate
def forward5(mydate):
    mysql = "select quotedate from stockquotes where symbol = 'SPY' and quotedate > '"+mydate+"' order by quotedate limit 5"
    print(mysql)
    cursor.execute(mysql)
    newdate = str(cursor.fetchall()[4][0])
    return newdate
def deletecandidate (mydate,symbol):
    mybefore = get30daysbefore(mydate)
    myafter = get30daysafter(mydate)
    print(mybefore, myafter)
    mysql = "delete from candidates where symbol = '" + symbol + "' and mydate > '" + str(
        mybefore) + "' and mydate<'" + str(myafter) + "'"
    print(mysql)
    cursor.execute(mysql)
    cnx.commit()

def entertrtade(entrydate,exitdate,entryval,exitval, shares,profit,symbol):
    mysql = "insert into trades (entrydate,exitdate,entryval,exitval,shares,profit,symbol) values ('"+str(entrydate)+"','"+str(exitdate)+"',"+str(entryval)+","+str(exitval)+","+str(shares)+","+str(profit)+",'"+symbol+"')"
    print (mysql)
    cursor.execute(mysql)
    mybefore = get30daysbefore(entrydate)
    myafter = get30daysafter(exitdate)
    print (mybefore,myafter)
    mysql = "delete from candidates where symbol = '"+symbol+"' and mydate > '"+str(mybefore)+"' and mydate<'"+str(myafter)+"'"
    print (mysql)
    cursor.execute(mysql)
    cnx.commit()

