import time
import sys
import RPi.GPIO as GPIO
from SimpleCV import *
cam = Camera () #setup the camera
#disp = Display()
lastImg =cam.getImage()
#lastImg.show()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

print sys.argv[1]
while True:  #disp.isDone():
    newImg = cam.getImage()
    trackImg = newImg - lastImg # diff the image
    if len(sys.argv)==1:
    	blobs = trackImg.findBlobs(20) #use adaptive blob detection
    else:
	blobs = trackImg.findBlobs(float(sys.argv[1])) #use adaptive blob detection
    now = int(time.time())

    #if blobs are found then motion has occured
    if blobs:
        print blobs
        newImg.save("/home/pi/Soc_Prosjekt/CameraImage/alarmphoto.jpg")
        lastImg = newImg #update the image
        GPIO.output(17,GPIO.HIGH)
	time.sleep(5);
        GPIO.output(17,GPIO.LOW)
