import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, timedelta

cred = credentials.Certificate('raspihome.json')

firebase_admin.initialize_app(cred, {
  'projectId': "raspihome-74f96",
})

db = firestore.client()

def getData():
    x = datetime.today() - timedelta(days=3)
    docs = db.collection(u'sensorData').where('timestamp', u'>=', x).stream();

    data = {'Humidity': [], 'Temperature': [], 'Timestamp': []}


    for doc in docs:
        #Catch outlier; Sometimes the sensor provides values with 140% Humidity and 12 °C
        if(doc.get("humidity")>=100):
            pass
        else:
            data['Humidity'].append(doc.get("humidity"))
            data['Temperature'].append(doc.get("temperatur"))
            data['Timestamp'].append(doc.get("timestamp"))

    return data
