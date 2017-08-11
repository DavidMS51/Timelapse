# Simple timelapse application
# David Saul 2017

# simple camera using Pi
from time import sleep
from picamera import PiCamera


# setup LDR, note we are not using the dedicated LDR function
# this removes the need for any additional components
from gpiozero import InputDevice
LDR = InputDevice(21,pull_up=True)


import datetime                 # for real time
from datetime import datetime   # for real time numbers

import os



def takepic():				#take a pic
	print "Taking picture"
#	camera.annotate_text = "Updated @"+ datetime.now().strftime('%H:%M on %a %d %b %Y ')
	camera.start_preview()
        sleep(.5)
        camera.capture('/home/pi/cabin_image.jpg')
	print "Picture taken"
        camera.stop_preview()


def arkcopy():					# make arkive copy of all pics
	#date stamp
        filename = "cabin_image_"+datetime.now().strftime('%H%M%S%d%m%Y')+".jpg"
	#make copy
	os.system("cp /home/pi/cabin_image.jpg /home/pi/picark/"+filename)
        return

	


# setup camera and resolution
camera = PiCamera()
camera.resolution = (1024, 786)
#camera.led = False

#camera.annotate_text = "First Picture"
c = 0					# counter variable
d = 0					# total pics taken
e = 0					# counter for time to next pic func
wdate = 10				# upload interval in minutes		

while True:
	while LDR.is_active == False:
		print "Too dark for picures"
		sleep(10)			
			

#	os.system('clear') 
	print "mins to next Pic =",wdate-e
	if c % wdate == 0:                  # check for update time
		takepic() 
		d=d+1
		print "Total pics taken =",d
		arkcopy()
		e=0
	e=e+1
	c=c+1
	sleep(60)



