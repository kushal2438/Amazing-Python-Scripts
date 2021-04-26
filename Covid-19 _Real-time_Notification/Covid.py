from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notify_user(title, message):
    notification.notify(
    title = title,
    message = message,
    app_icon = "./Covid-19_Real-time_Notification/Notify_icon.ico" ,
    timeout = 3)
    
def getInfo(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    while True:
        HtmlData = getInfo('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(HtmlData, 'html.parser')
    
        myData=""
        for tr in soup.find('table').find('tbody')[1].find_all('tr'):
            myData += tr.get_text()
        
        myData = myData[1:]
        itemList = myData.split("\n\n")
    
        states = list(map(str,input("Enter the name of state:"))
        for item in itemList[0:22]:
            dataList = item.split('\n')
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of Covid-19'
                ntext = f"{dataList[1]} Total: {datalist[2][0]}\n Cured: {datalist[4][0]}\n Deaths: {datalist[6][0]}"
                notify_user(nTitle, ntext)
        time.sleep(3600)