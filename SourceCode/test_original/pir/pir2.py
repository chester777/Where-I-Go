import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

try :
	while True :
		if GPIO.input(23) :
			#GPIO.output(12, True)
			time.sleep(1)
			print "On"
		else :
			#GPIO.output(12, False)
			time.sleep(1)
			print "Off"
except :
	GPIO.cleanup()		
