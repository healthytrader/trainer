import sys
import trainerhelper
import candlestick1
import numpy
symbol=""
mydate=""
myentry=""
myexit=""
entryval=0
exitval=0
ishares=0
bintrade=False
direction=""


def printhelp():
    print ("exit, help, g-getcandidate,d-show chart,d1-showshorttermchart st-status,l-tradelong,<nbr>-forwarddays,x-exittrade")

def tradelong (mysymbol,mydate):
    global bintrade
    global entryval
    global myentry
    global direction
    print("going long:"+mysymbol+" on:"+mydate)
    myentry= trainerhelper.forward1(mydate)
    entryval = trainerhelper.getopenprice(myentry,mysymbol)
    bintrade=True
    direction="Long"
    print(symbol, mydate, bintrade, myentry, entryval,direction)

def tradeshort(mysymbol, mydate):
        global bintrade
        global entryval
        global myentry
        global direction
        print("going short:" + mysymbol + " on:" + mydate)
        myentry = trainerhelper.forward1(mydate)
        entryval = trainerhelper.getopenprice(myentry, mysymbol)
        bintrade = True
        direction = "Short"
        print(symbol, mydate, bintrade, myentry, entryval, direction)


def exittrade(mysymbol,mydate):
    global bintrade
    global exitval
    global myexit
    global direction
    global myentry
    global entryval
    global ishares
    print("gxiting:" + mysymbol + " on:" + mydate)
    myexit = trainerhelper.forward1(mydate)
    exitval = trainerhelper.getopenprice(myexit, mysymbol)
    print (exitval)
    bintrade = False
    if direction=="Long":
        profit = exitval - entryval
        profit = profit * ishares
    elif direction=="Short":
        profit = entryval - exitval
        profit = profit * ishares
    direction = ""
    print(symbol, mydate, bintrade, myentry, entryval, direction,"Profit",profit)
    trainerhelper.entertrtade(myentry, myexit, entryval, exitval, ishares, profit,mysymbol)
def exittradeclose(mysymbol,mydate):
    global bintrade
    global exitval
    global myexit
    global direction
    global myentry
    global entryval
    global ishares
    print("gxiting:" + mysymbol + " on:" + mydate)
    myexit = mydate
    exitval = trainerhelper.getcloseprice(myexit, mysymbol)
    print (exitval)
    bintrade = False
    if direction=="Long":
        profit = exitval - entryval
        profit = profit * ishares
    elif direction=="Short":
        profit = entryval - exitval
        profit = profit * ishares
    direction = ""
    print(symbol, mydate, bintrade, myentry, entryval, direction,"Profit",profit)
    trainerhelper.entertrtade(myentry, myexit, entryval, exitval, ishares, profit,mysymbol)

def evaluate():
    profit = trainerhelper.getprofits()
    p1 = numpy.array(profit)
    mean = numpy.mean(p1)
    median = numpy.median(p1)
    print ("median=",median,"average=",mean)
def showchartsmall(mysymbol,mydate2):
    #try:
        if len(mysymbol)<2  or len(mydate2)<2:
            print ("No Candidate Yet 1")
        else:
            print("showing chart for:"+mysymbol+" on:"+mydate2)
            mydate2 = trainerhelper.get50daysbefore(mydate2)
            candlestick1.visualizesmall(mysymbol,mydate2)
def showchartlarge(mysymbol,mydate2):
    #try:
        if len(mysymbol)<2  or len(mydate2)<2:
            print ("No Candidate Yet 1")
        else:
            print("showing chart for:"+mysymbol+" on:"+mydate2)
            mydate2 = trainerhelper.get500daysbefore(mydate2)
            candlestick1.visualizelarge(mysymbol,mydate2)

def evaluatepnl():
    myr = trainerhelper.getprofitsOutput()
    for myx in myr:
        print (str(myx[0]))

def showchart(mysymbol,mydate2):
    #try:
        if len(mysymbol)<2  or len(mydate2)<2:
            print ("No Candidate Yet 1")
        else:
            print("showing chart for:"+mysymbol+" on:"+mydate2)
            mydate2 = trainerhelper.get150daysbefore(mydate2)
            candlestick1.visualize(mysymbol,mydate2)
   # except:
     #   print("No Candidate Yet 2")

while True:
    command = input("command: ")
    print (command)
    if command=="exit":
        sys.exit()
    elif command=="help":
        printhelp()
    elif command=="g":
        symbol,mydate,ishares= trainerhelper.getcandidate()
        print (symbol,mydate)
    elif command=="st":
        print (symbol,mydate,bintrade,myentry,entryval,direction,ishares)
    elif command=="d":
        showchart(symbol,mydate)
    elif command=="ds":
        showchartsmall(symbol,mydate)
    elif command=="dl":
        showchartlarge(symbol,mydate)
    elif command=="l":
        if (bintrade==False):
            tradelong(symbol,mydate)
    elif command=="x":
        exittrade(symbol,mydate)
    elif command=="xc":
        exittradeclose(symbol,mydate)
    elif command=="delete":
        trainerhelper.deletecandidate (mydate,symbol)
        #sys.exit()
    elif command=="sh":
        if (bintrade==False):
            tradeshort(symbol,mydate)
    elif command=="1":
        mydate = trainerhelper.forward1(mydate)
        showchart(symbol, mydate)
    elif command=="3":
        mydate = trainerhelper.forward3(mydate)
        showchart(symbol, mydate)
    elif command == "5":
        mydate = trainerhelper.forward5(mydate)
        showchart(symbol, mydate)
    elif command=="eval":
        evaluate()
    elif command=="evalpnl":
        evaluatepnl()

