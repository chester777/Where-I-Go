import RPi.GPIO as GPIO
import time

print "PWM : Pulse Width Module Example"

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18,50)
p.start(0)

for x in range(0, 4) :
	print ("count = " + str(x))
	for dc in range(0, 101, 2) :
		p.ChangeDutyCycle(dc)
		time.sleep(0.1)
	
	for dc in range(100, -1, -2) :
		p.ChangeDutyCycle(dc)
		time.sleep(0.1)

p.stop()

print "GPIO.cleanup()"
GPIO.cleanup()
