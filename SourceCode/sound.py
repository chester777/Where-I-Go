import os

def beef_out(info) :
	if info["LH"] == 0 :
		os.system("mpg123 -a bluetooth ~/project/sound/beep/LH_0.mp3")
	elif info["LH"] == 1 :
		os.system("mpg123 -a bluetooth ~/project/sound/beep/LH_1.mp3")
	elif info["LH"] == 2 :
		os.system("mpg123 -a bluetooth ~/project/sound/beep/LH_2.mp3")

	if info["LL"] == 0 :
		os.system("mpg123 -a bluetooth ~/project/sound/beep/LL_0.mp3")
	elif info["LL"] == 1 :
		os.system("mpg123 -a bluetooth ~/project/sound/beep/LL_1.mp3")
	elif info["LL"] == 2 :
		os.system("mpg123 -a bluetooth ~/project/sound/beep/LL_2.mp3")

	if info["RH"] == 0 :
		os.system("mpg123 -a bluetooth ~/project/sound/beep/RH_0.mp3")
	elif info["RH"] == 1 :
		os.system("mpg123 -a bluetooth ~/project/sound/beep/RH_1.mp3")
	elif info["RH"] == 2 :
		os.system("mpg123 -a bluetooth ~/project/sound/beep/RH_2.mp3")

	if info["RL"] == 0 :
		os.system("mpg123 -a bluetooth ~/project/sound/beep/RL_0.mp3")
	elif info["RL"] == 1 :
		os.system("mpg123 -a bluetooth ~/project/sound/beep/RL_1.mp3")
	elif info["RL"] == 2 :
		os.system("mpg123 -a bluetooth ~/project/sound/beep/RL_2.mp3")

def name_out(name) :
	os.system("mpg123 -a bluetooth ~/project/sound/name/detect_human.mp3")
	if name == "Lee Gyu Jin" :
		os.system("mpg123 -a bluetooth ~/project/sound/name/human_gyujin.mp3")
	elif name == "Lee Jong Chan" :
		os.system("mpg123 -a bluetooth ~/project/sound/name/human_jongchan.mp3")
	elif name == "Kim Min Jae" :
		os.system("mpg123 -a bluetooth ~/project/sound/name/human_minjae.mp3")
	else :
		os.system("mpg123 -a bluetooth ~/project/sound/name/human_stranger.mp3")