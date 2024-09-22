#imports
from selenium import webdriver
import datetime, time, json

elemNM = None


#craft birthday wish
def wishBirthday(name):
    return "Happyy Birthdayy " + name + "!!"


def getJSON(file, birthDate, birthMonth, currDate, currMonth):
    data = json.load(file)
    returnData = []
    
    for i in data:
        if (i[birthDate] == currDate and i[birthMonth] == currMonth):
            returnData.append(i["name"])
    
    return returnData


data = open("birthdays.json","r")
print("Script Running")

while True:
    try:
        currDateTime = datetime.datetime.now()
        nameValues = getJSON(data, "birth_date" , "birth_month", str(currDateTime.day), str(currDateTime.month))
    
    except json.decoder.JSONDecodeError:
        continue
    
    if nameValues != []:
        break


#opening whatsapp on chrome
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("user-data-C:\\Users\\bhava\\AppData\\Local\\Google\\Chrome\\User Data\\Default") 
driver = webdriver.Chrome(executable_path ="C:\\Users\\bhava\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe", options = chropt)
driver.get("https://web.whatsapp.com/")


time.sleep(10)


print(nameValues)


for x in nameValues:
    try:
        eleNM = driver.find_element_by_xpath('//span[@title ="{}"]'.format(inp))
    except Exception as ex:
        print(ex)