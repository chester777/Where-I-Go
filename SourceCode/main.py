import gpioHW
import sound
import bluetooth
import humanrec

info = {}
#bluetooth.pairing("NB-K1")

print "start"

try :
	while True :

		info["RH"] = gpioHW.distance_level(gpioHW.RH_trig, gpioHW.RH_echo)
		info["RL"] = gpioHW.distance_level(gpioHW.RL_trig, gpioHW.RL_echo)
		info["FH"] = gpioHW.distance_level(gpioHW.FH_trig, gpioHW.FH_echo)
		info["FL"] = gpioHW.distance_level(gpioHW.FL_trig, gpioHW.FL_echo)
		info["LH"] = gpioHW.distance_level(gpioHW.LH_trig, gpioHW.LH_echo)
		info["LL"] = gpioHW.distance_level(gpioHW.LL_trig, gpioHW.LL_echo)

		#sound.beef_out(info)
		gpioHW.motor_vibrate(info)
		#if gpioHW.button_detected() == True :


except :
	print "except"
	gpio.cleanup()