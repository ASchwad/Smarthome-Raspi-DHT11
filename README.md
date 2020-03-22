# Smarthome-Raspi-DHT11
Get room temperature and humidity with DHT11 and persist data in Firebase. Pull Data from Firebase and visualize Data by using the Dash Framework

## How to run
1. Follow the [Adafruit Library](https://github.com/adafruit/Adafruit_Python_DHT) instructions to get Sensor data. 
2. Run the Dash App
3. Run the Notification Manager

(The firebase credential file is excluded and the telegram token is revoked)

## Technology
* Raspberry Pi with DHT 11, evaluation with Adafruit Library
* I used Google Firebase (Cloud Firestore) to store and read the sensor data. They have a good api and reasonable free plans.
* Dash for Data Visualization
* Telegram API for notifications (e.g. Open the window)
