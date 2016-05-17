import RPi.GPIO as GPIO
import time

print "PWM : Pulse Width Module Example"

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18,1)

p.start(10)

raw_input("Press any key to change frequency (2Hz):")

p.ChangeFrequency(2)

raw_input("Press any key to change frequency (5Hz) :")

p.ChangeFrequency(5)

raw_input("Press any key to quit:")
p.stop()

print "GPIO.cleanup()"
GPIO.cleanup()
