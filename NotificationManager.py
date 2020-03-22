import requests
import time
from FirebaseManager import getData

def sendNotification():
    token = '1053655623:AAEhGfDZUKci52cdryARXfK0PnADw1IP5O4'

    chatId = -460683381

    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chatId, 'text': 'Luftfeuchtigkeit: ' + str(40) + "% seit über einer Stunde. Lüft mal..."}
    requests.post(url, data).json()

while(1):
    data = getData(1/24)
    humidityData = data["Humidity"]
    humidityData = humidityData[-4:]

    notificationBool = False

    for value in humidityData:
        if(value < 40):
            notificationBool = False
            print(notificationBool)
            break

    if(notificationBool):
        print(notificationBool)
        sendNotification()
        #anti spam: send message only every 3 hours at max
        time.sleep(60*180)
    else:
        time.sleep(60 * 15)