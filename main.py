import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import time 
import sensor #import my sensor module

realTimeAppURL = "https://arduino-testing-16ba1-default-rtdb.europe-west1.firebasedatabase.app/"

cred = credentials.Certificate('serviceAccountKey.json') #import realtime configure json file
default_app = firebase_admin.initialize_app(cred,{"databaseURL": realTimeAppURL})

ref = db.reference("flowerpot") #Reference point created


while True:
    value = sensor.getSensorValue()
    ref.set({"humidity":value}) #a row was created for the humidity
    print(value)
    time.sleep(30) #wait 30 seconds


    

