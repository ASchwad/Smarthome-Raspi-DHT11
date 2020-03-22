import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import time
#TODO: Catch non readable sensor output to continue script; Change evaluation time to every 15 minutes

#Has to be run with 'python3.7 SensorScript.py 11 4' for the used pins on the raspberry pi
cred = credentials.Certificate('raspihome.json')

firebase_admin.initialize_app(cred, {
  'projectId': "raspihome-74f96",
})

db = firestore.client()

# Parse command line parameters.
sensor_args = {'11': Adafruit_DHT.DHT11,
               '22': Adafruit_DHT.DHT22,
               '2302': Adafruit_DHT.AM2302}
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
    print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
    sys.exit(1)

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
while (1):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        timestamp = datetime.datetime.now()

        doc_ref = db.collection(u'sensorData').document(timestamp)
        doc_ref.set({
            u'temperatur': temperature,
            u'humidity': humidity,
            u'timestamp': timestamp
        })
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)
    #evaluate sensor every 10 minutes
    time.sleep(600)