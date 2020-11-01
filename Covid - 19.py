# it is just a simple covid update bot
# getting data from

import requests
from win10toast import ToastNotifier
import json
import time

def update():
    req = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = req.json() # receiving data from api
    test = f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast('Covid-19 Update', test, duration = 20) # notification will be shown for 20 seconds 
        time.sleep(60)

update()