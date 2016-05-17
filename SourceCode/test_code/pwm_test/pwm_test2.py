import RPi.GPIO as GPIO
import time

print "PWM : Pulse Width Module Example"

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

p = GPIO.PWM(14,50)
p.start(0)

for x in range(0, 10) :
	print ("count = " + str(x))
	p.ChangeDutyCycle(100)
	time.sleep(1)
	p.ChangeDutyCycle(50)
	time.sleep(1)

p.stop()

print "GPIO.cleanup()"
GPIO.cleanup()
