import subprocess
import time
import RPi.GPIO as GPIO
input_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin, GPIO.IN)

while True:
    if (GPIO.input(input_pin)):
        print('Button Pressed')
        print("Get ready with your webcam")
        print('Taking snap in next 3 seconds')
        time.sleep(3)  
        print("Taking snap")
        subprocess.call(['fswebcam', '-r', '720x340', 'ZERO.jpg'])
        print("Thresholding image")
        subprocess.call(['convert', './ZERO.jpg', '-threshold', '+20%', 'speech.jpg'])
        print("Performing OCR")
        subprocess.call(['tesseract', 'speech.jpg', 'speech'])
        print("The detected text is")
        subprocess.call(['cat', 'speech.txt'])
        print("Speaking text")
        subprocess.call('espeak -s 120 -ven ' + 'speech.txt' +'--stdout | aplay',shell=True)
GPIO.cleanup()

