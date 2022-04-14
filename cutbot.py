import RPi.GPIO as GPIO
import time
import requests
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
powercut = 1

while True:
    pin_status = GPIO.input(4)
    print(pin_status)
    time.sleep(1)
    if pin_status > powercut:
        print ("powercut ho gaya")
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print (current_time)
        url = "https://maker.ifttt.com/trigger/<app name>/json/with/key/UIHUHHUH*^^UHIH"
        url2 = "https://maker.ifttt.com/trigger/<app name 2>/json/with/key/JGJHGYUUYU&*^*^*GHJGJ"
        res = requests.get(url)
        res2 = requests.get(url2)
        time.sleep(300)
        print(res.status_code)
        print(res2.status_code)
      
    powercut = pin_status
