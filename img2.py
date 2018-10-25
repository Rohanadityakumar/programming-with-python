import RPi.GPIO as GPIO
import time
import os
a=0
GPIO.setmode(GPIO.BCM)
pirPin=6
GPIO.setup(pirPin, GPIO.IN)
counter=1
time.sleep(4)
while counter<=2:
    if GPIO.input(pirPin):
        print("motion detected")
        os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/pi/rohan/"+str(a)+".jpg")
        print("picture taken")
        counter = counter+1
        a=a+1
print("testing")
exit()

