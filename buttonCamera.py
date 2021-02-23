from picamera import PiCamera
from time import sleep
from gpiozero import Button
from datetime import datetime
from datetime import time

button = Button(4)
camer = PiCamera()

camera.start_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        sleep(2)
        date = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        camera.annotate_text = date
        
        camera.capture('/home/pi/SavedImages/image'+date+'.jpg')
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break