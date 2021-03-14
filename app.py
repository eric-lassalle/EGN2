from flask import Flask, Markup
from flask import render_template
from flask import request, redirect


'''
Start script
 . venv/bin/activate
 python -m flask run
 bandi made this comment

 KIA
 MIA
 WIA

'''


class Message:
  def __init__(self, timeStamp, name, msg):
    self.timeStamp = timeStamp
    self.name = name
    self.msg = msg



timestampBool = False
nameBool = False
msgBool = False

timeStampInfo = ""
nameInfo = ""
msgInfo = ""

#Eric's Changes
labelInfo = ""
z = 10
#---------------

container = []

#Eric's Changes
bar_label = []
bar_value = []
#---------------

# for line in FileContent:
#   #
#   if "[" in line: #This next part will be a time stamp...
#     #record the next segment of data



with open("./data/data.txt") as fileobj:
  for line in fileobj:
    for char in line: 
      #  print(char)

      if char == "]":
        timestampBool = False

      elif char == "<":
        nameBool = True

      elif char == ">":
        nameBool = False
        msgBool = True

      elif char == "[":
        timestampBool = True
        
        if msgBool == True:
          container.append(Message(timeStampInfo, nameInfo, msgInfo))

          #Eric's Changes
          if labelInfo != "":
            bar_label.append(labelInfo)
          #---------------

          #re initialize temp vars
          timeStampInfo = ""
          nameInfo = ""
          msgInfo = ""
          msgBool = False

          #Eric's changes
          labelInfo = ""
          z = 10
          #---------------

      else:
        if timestampBool == True:
          timeStampInfo += char

          #Eric's changes
          if z > 0:
            if char != "0" and char != "1" and char != "2" and char != "3" and char != "4" and char != "5" and char != "6" and char != "7" and char != "8" and char != "9" and char != "/":
              z = 0
              labelInfo = ""
            else: 
              labelInfo += char
              z -= 1
          #---------------

        #  print(timeStampInfo)

        if nameBool == True:
          nameInfo += char
        #  print(nameInfo)

        if msgBool == True:
          msgInfo += char
        #  print(msgInfo)

container.append(Message(timeStampInfo, nameInfo, msgInfo)) #after exiting the loop, the temp variables are still stored so we can append the final message...

#Eric's Changes
def valueCounter():
  seen = {}
  j = 0
  for i in range(len(bar_label)):
    temp = bar_label[i]
    if temp in seen:
      bar_value[j] += 1
      seen[temp] += 1
    else:
      if i > 0:
        j += 1
      bar_value.append(1)
      seen[temp] = 1
  return seen.keys()
#---------------

def showSitreps(): #function that prints all sitreps of the given file
  ret = []
  for i in range(len(container)):
    temp = container[i]
    if temp.name == "115 FAB BTL NCO":
      if "SITREP" in temp.msg:

        ret.append(temp)
  return ret



def recentSitrep(): #function that prints all sitreps of the given file
  
  for i in range(len(container)):
    temp = container[i]
    if temp.name == "115 FAB BTL NCO":
      if "SITREP" in temp.msg:
          mostRecent = temp
    

        
  return mostRecent


def allSaluteReport():
    ret = [] 
    for i in range(len(container)):
        temp = container[i]
        if temp.name == "115 FAB BTL NCO":
            ret.append(temp)
    return ret
      
def recentSalute():
    for i in range(len(container)):
        temp = container[i]
        if temp.name == "115 FAB BTL NCO":
            if "SALUTE REPORT" in temp.msg:
                mostRecent = temp


    return mostRecent     

def authors():
    seen = {}

    for i in range(len(container)):
        temp = container[i]
        if temp.name in seen:
            seen[temp.name] += 1
        else:
            seen[temp.name] = 0
    return len(seen)

def ammoStat(): #displays most recent ammo status
  for i in range(len(container)):
    temp = container[i]
    if temp.name == "115 FAB BTL NCO":
      if "SITREP" in temp.msg:
        if "Ammo Status: Green" in temp.msg:
          ammo = "Green"
        elif "Ammo Status: Red" in temp.msg:
          ammo = "Red"
        elif "Ammo Status: Amber" in temp.msg:
          ammo = "Amber"
        elif "Ammo Status: Black" in temp.msg:
          ammo = "Black"
        elif "Ammo Status: N.A" in temp.msg:
          ammo = "Not Available"

  return ammo

def fuelStat(): #displays most recent fuel status 
  for i in range(len(container)):
    temp = container[i]
    if temp.name == "115 FAB BTL NCO":
      if "SITREP" in temp.msg:
        if "Fuel Status: Green" in temp.msg:
          fuel = "Green"
        elif "Fuel Status: Amber" in temp.msg:
          fuel = "Amber"
        elif "Fuel Status: Black" in temp.msg:
          fuel = "Black"
        elif "Fuel Status: Red" in temp.msg:
          fuel = "Red"
        elif "Fuel Status: N.A" in temp.msg:
          fuel = "Not Available"

  return fuel

def staffStat(): #displays most recent personnel status 
  for i in range(len(container)):
    temp = container[i]
    if temp.name == "115 FAB BTL NCO":
      if "SITREP" in temp.msg:
        if "Personnel Status: Red" in temp.msg:
          personnel = "Red"
        elif "Personnel Status: Green" in temp.msg:
          personnel = "Green"
        elif "Personnel Status: Amber" in temp.msg:
          personnel = "Amber"
        elif "Personnel Status: Black" in temp.msg:
          personnel = "Black"
        elif "Personnel Status: N.A" in temp.msg:
          personnel = "Not Available"

  return personnel


def getImportantNumbers():

  '''
   KIA
   MIA
    WIA
 '''
  kiaMsg, miaMsg, wiaMsg, size = [], [], [], len(container)
  

  for i in range(size):
      msg = container[i].msg
      if 'kia' in msg or 'KIA' in msg:
        kiaMsg.append(msg.upper())
      elif 'mia' in msg or 'MIA' in msg:
        miaMsg.append(msg.upper())
      elif 'wia' in msg or 'WIA' in msg:
        wiaMsg.append(msg.upper())
      else:
        pass
  
  
  m1, k1, w1 = parseMsgScraper(kiaMsg)
  m2, k2, w2 = parseMsgScraper(wiaMsg)
  


  
  

  
  # print(miaMsgFinal)
  # print(wiaMsgFinal)

  #kiaInt, miaInt, wiaInt = parseIntMsgScrapper(kiaMsgFinal), parseIntMsgScrapper(miaMsgFinal), parseIntMsgScrapper(wiaMsgFinal)
  kiaIntArr1 = parseIntMsgScrapper(k1)
  k1Int = sum(kiaIntArr1)
  kiaIntArr2 = parseIntMsgScrapper(k2)
  k2Int = sum(kiaIntArr2)


  miaIntArr1 = parseIntMsgScrapper(m1)
  m1Int = sum(miaIntArr1)

  miaIntArr2 = parseIntMsgScrapper(m2)
  m2Int = sum(miaIntArr1)
  
  



  wiaIntArr1 = parseIntMsgScrapper(w1)
  w1Int = sum(wiaIntArr1)

  wiaIntArr2 = parseIntMsgScrapper(w2)
  w2Int = sum(wiaIntArr1)
  
  


  total_KIA = k1Int + k2Int
  total_WIA = w1Int + w2Int
  total_MIA = m1Int + m2Int

  # print("total kia: " + str(total_KIA) + " total wia: " + str(total_WIA) + " total mia:" + str(total_MIA))
  return total_KIA, total_WIA, total_MIA



def parseMsgScraper(messages):
  # init
  size= len(messages)
  miaRet, kiaRet, wiaRet = [], [], []

  
  for i in range(size):
    msg = messages[i]
    
    for j in range(len(msg)):
      msgChar = msg[j]
      if msgChar == 'M':
          if 'MIA' in msg[j:j+4]:
            miaRet.append(msg[j:j+10])
          
      elif msgChar == 'K':
          if 'KIA' in msg[j:j+4]:
            kiaRet.append(msg[j:j+10])
      elif msgChar == 'W':
          if 'WIA' in msg[j:j+4]:
            wiaRet.append(msg[j:j+10])
          
      else:
        pass
      
  return miaRet, kiaRet, wiaRet
    
def parseIntMsgScrapper(messages):
  total = []
  for message in messages:
    for msg in message.split():
      if msg.isdigit():
        total.append(int(msg))  

  return total
  
def userSearch(user):  # outputs all messages from an inputted user
    ret = []
    for i in range(len(container)):
        temp = container[i]
        if temp.name == user:
            ret.append(temp)
    return ret  # returns all the messages containing the user in the .name.
  
# for i in range(len(sitreps)):
#     temp = sitreps[i]
#     print("\n\nSITREP report at: ", temp.timeStamp)
#     print("Content of SITREP: ", temp.msg)

def getUserInfo(): 
  seen = {}
  for i in range(len(container)):
    temp = container[i]
    if temp.name in seen:
      seen[temp.name] = seen[temp.name] + 1
    else:
      seen[temp.name] = 1
  return seen
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('./index.html')

'''
@app.route("/upload-txt", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["text"]

            print(image)

            return redirect(request.url)


    return render_template("./index.html")
'''

@app.route("/processing", methods=["GET", "POST"])
def processing():

    if request.method == "GET":

        return render_template("./processing.html")

    return render_template("./index.html")


@app.route("/final", methods=["GET", "POST"])
def final():
    total = len(container)
    total_KIA, total_WIA, total_MIA = getImportantNumbers()
    first = container[0].timeStamp.split()
    last = container[total - 1].timeStamp.split()
    first = first[0]
    last = last[0]
    print(first)
    print(last)
    authorTotal = authors()
    mostRecent = recentSitrep()
    salute = recentSalute()
    personnel = staffStat()
    ammo = ammoStat()
    fuel = fuelStat()
    
    return render_template("./final.html", firstDate = first, lastDate = last,KIA = total_KIA, MIA = total_MIA, WIA = total_WIA, totalMessages=total, totalAuthors=authorTotal, sitRep = mostRecent, saluteReport = salute, ammoStatus = ammo, fuelStatus = fuel, personnelStatus = personnel)


@app.route("/allSitreps", methods=["GET", "POST"])
def allSitreps():
    sitreps = showSitreps()
    

    return render_template("./allSitreps.html", finalSitreps=sitreps)


@app.route("/allReports", methods=["GET", "POST"])
def reports():
    allReports = allSaluteReport()
    for report in allReports:
        if "ACK" in report.msg:
            allReports.remove(report)

    return render_template("./allReports.html", reports=allReports)


@app.route("/allMessages", methods=["GET", "POST"])
def allMessages():
    

    return render_template("./allMessages.html", messages=container)

  
@app.route("/searchUser", methods=["GET", "POST"])
def searchUser():
    if request.method == "POST":
        user = request.form['user']

    userList = userSearch(user)
    if userList == []:
        userList == ""

    return render_template("./searchUser.html", userList=userList)  

@app.route("/userInfo", methods=["GET", "POST"])
def userInfo():
    seen = getUserInfo()
    

    return render_template("./userInfo.html", people = seen)  
   
   
   
# updates carousel with messages
@app.route("/carousel", methods = ["GET", "POST"])
def carousel():
    total = len(container)
    
    
    return render_template("./carousel.html", totalMessages = total, messages = container )   

# Test page for chart
@app.route("/chart", methods = ["GET", "POST"])
def chart():
    test = 0
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template("./chart.html", values=values, labels=labels, legend=legend)

#Eric's Changes
@app.route("/barChart", methods = ["GET", "POST"])
def barChart():
    test = 0
    legend = 'Message Count'
    labels = valueCounter()
    values = bar_value
    return render_template("./barChart.html", values=bar_value, labels=labels, legend=legend, title="Message Count for Each Day")
 
 
  
    
    
