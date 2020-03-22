import requests

def sendNotification():
    token = ''

    chatId = -460683381

    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chatId, 'text': 'Luftfeuchtigkeit: ' + str(40) + "% seit über einer Stunde. Lüft mal..."}
    requests.post(url, data).json()