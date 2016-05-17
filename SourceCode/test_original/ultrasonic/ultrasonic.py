import RPi.GPIO as gpio
import time

def ultra_distance(trig, echo) :
	gpio.output(trig, False)
	time.sleep(0.5)

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

trig1 = 15
echo1 = 14

print "start"

gpio.setup(trig1, gpio.OUT)
gpio.setup(echo1, gpio.IN)

try :
	while True :
		
		print "distance 1 : ", ultra_distance(trig1, echo1), "cm"

except :
	gpio.cleanup()
