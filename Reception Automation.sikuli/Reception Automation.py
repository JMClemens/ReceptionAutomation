import time

totalSlides = 0
totalSeconds = 0

def setupMenu():
    choice = input("Is the solar information already visible in Google chrome? (yes or no)")
    if choice == "yes":
        getInfo()
        openPpt()
        eventLoop()
    else:
        solarLogin()
        getInfo()
        openPpt()
        eventLoop()
            

def solarLogin():
    find("1517421986932.png")
    click("1517421986932.png")
    time.sleep(5)
    find("1517422027763.png")
    click("1517422027763.png")
    type(r'https://monitoring.solaredge.com/solaredge-web/p/login' + Key.ENTER)
    time.sleep(5)
    find("1516897428437.png")
    click("1516897435753.png")
    type(r'bbccsolar@gmail.com' + Key.TAB + r'bbccsolar1')
    find("1516897482185.png")
    click("1516897487308.png")

def displaySolar():
    pass

def getInfo():
    global totalSlides
    numSlides = input("How many slides are in your powerpoint?")
    totalSlides = numSlides
    videoExists = input("Is there a video in the powerpoint? (yes or no)")
    if videoExists == "yes":
        getSeconds()
            
def getSeconds():
    global totalSeconds 
    videoLength = input("How long is the video? (minutes:seconds)")
    ftr = [60,1]
    seconds = sum([a*b for a,b in zip(ftr, map(int, videoLength.split(':')))])
    totalSeconds = seconds

def openPpt():
    find("1516900388456.png")
    click("1516900394563.png")
    find("1516900419643.png")
    click("1516900428029.png")
    find("1516900600748.png")
    doubleClick(Pattern("1516900610548.png").targetOffset(-3,-32))

    playPpt()
    
def playPpt():
    time.sleep(5)
    find("1516900871740.png")
    doubleClick("1516900876773.png")
    find("1516900921661.png")
    click("1516900988964.png")
    s = 1 
    global totalSlides
    tSlides = totalSlides
    global totalSeconds
    tSecs = totalSeconds
    cntrl = False 
    print(s)
    print("total slides" + str(tSlides))
    print("total seconds" + str(tSecs))
    while not cntrl:
        if s == tSlides:
            print("if stmt")
            cntrl = True
            type(Key.ESC)
            break;
        elif exists("1517425162535.png"):
            print("elif stmt")
            hover(Location(800, 459))
            find("1517424868409.png")
            click(Pattern("1517424868409.png").targetOffset(-2,2))
            time.sleep(tSecs)
            click(Location(1583, 16))
            s = s + 1
            print(s)
        else:
            print("else stmt")
            time.sleep(5)
            click(Location(1583, 16))
            s = s + 1
            print(s)
        

def eventLoop():
    pass

setupMenu()


