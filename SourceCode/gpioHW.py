import RPi.GPIO as gpio
import time
import os

gpio.setmode(gpio.BCM)

Button = 14
Motor_out = 15

RH_trig = 2
RH_echo = 3

RL_trig = 23
RL_echo = 22

FH_trig = 27
FH_echo = 18

FL_trig = 25
FL_echo = 9

LH_trig = 17
LH_echo = 4

LL_trig = 24
LL_echo = 10

gpio.setup(Motor_out, gpio.OUT)

Motor = gpio.PWM(Motor_out, 50)
Motor.start(0)

gpio.setup(Button, gpio.IN, pull_up_down=gpio.PUD_UP)

gpio.setup(RH_trig, gpio.OUT)
gpio.setup(RH_echo, gpio.IN)

gpio.setup(RL_trig, gpio.OUT)
gpio.setup(RL_echo, gpio.IN)

gpio.setup(FH_trig, gpio.OUT)
gpio.setup(FH_echo, gpio.IN)

gpio.setup(FL_trig, gpio.OUT)
gpio.setup(FL_echo, gpio.IN)

gpio.setup(LH_trig, gpio.OUT)
gpio.setup(LH_echo, gpio.IN)

gpio.setup(LL_trig, gpio.OUT)
gpio.setup(LL_echo, gpio.IN)

def distance_level(trig, echo) :
	gpio.output(trig, False)
	time.sleep(0.01)

	gpio.output(trig, True)
	time.sleep(0.01)
	gpio.output(trig, False)

	while gpio.input(echo) == 0 :
		pulse_start = time.time()

	while gpio.input(echo) == 1 :
		pulse_end = time.time()			

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17000
	distance = round(distance, 2)

	# specify figure is modified after test

	if 0 <= distance and distance < 100 :
		level = 0
	elif 100 <= distance and distance < 200 :
		level = 1
	elif 200 <= distance and distance < 300 :
		level = 2
	else :
		level = False

	return level

def button_detected() :
	if gpio.input(Button) == False : # if Button is pressed
		return True

def motor_vibrate(info) :
	if info["RH"] == 0 :
		Motor.ChangeFrequency(5)
	elif info["RH"] == 1 :
		Motor.ChangeFrequency(3)
	elif  info["RH"] == 2 :
		Motor.ChangeFrequency(1)
	else :
		Motor.ChangeFrequency(0)

	if info["RL"] == 0 :
		Motor.ChangeFrequency(5)
	elif info["RL"] == 1 :
		Motor.ChangeFrequency(3)
	elif  info["RL"] == 2 :
		Motor.ChangeFrequency(1)
	else :
		Motor.ChangeFrequency(0)