import RPi.GPIO as gpio
import time

def distance_level(trig, echo) :

	gpio.output(trig, False)
	time.sleep(0.2)

	gpio.output(trig, True)
	time.sleep(0.00001)
	gpio.output(trig, False)

	while gpio.input(echo) == 0 :
		pulse_start = time.time()

	while gpio.input(echo) == 1 :
		pulse_end = time.time()			

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17000
	distance = round(distance, 2)

	return distance

gpio.setmode(gpio.BCM)

FL_trig = 20
FL_echo = 21

print "start"

gpio.setup(FL_trig, gpio.OUT)
gpio.setup(FL_echo, gpio.IN)

try :
	while True :

		print "distance : " + str(distance_level(FL_trig, FL_echo)) + "cm"

except :
	print "except"
	gpio.cleanup()