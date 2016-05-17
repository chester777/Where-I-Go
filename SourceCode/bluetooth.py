import os
import re

# Searching The Bluetooth Speaker
def pairing(bluetooth) :
	f = os.popen("hcitool scan | grep " + bluetooth) 
	speaker_mac = re.findall("\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}",f.read())

	os.system("sudo bt-device -c " + str(speaker_mac[0]))
	os.system("sudo bluez-simple-agent hci0 " + str(speaker_mac[0]))
	os.system("sudo hciconfig hci0 up")
	os.system("sudo bluez-test-device trusted " + str(speaker_mac[0]) + " yes")
	os.system("sudo bluez-test-audio connect " + str(speaker_mac[0]))