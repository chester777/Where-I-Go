import os

def speaker_out(info) :
	if info["LH"] == 0 :
		os.system("mpg123 -a bluetooth ./sound/LH_0.mp3")
	elif info["LH"] == 1 :
		os.system("mpg123 -a bluetooth ./sound/LH_1.mp3")
	elif info["LH"] == 2 :
		os.system("mpg123 -a bluetooth ./sound/LH_2.mp3")

	if info["LL"] == 0 :
		os.system("mpg123 -a bluetooth ./sound/LL_0.mp3")
	elif info["LL"] == 1 :
		os.system("mpg123 -a bluetooth ./sound/LL_1.mp3")
	elif info["LL"] == 2 :
		os.system("mpg123 -a bluetooth ./sound/LL_2.mp3")

	if info["RH"] == 0 :
		os.system("mpg123 -a bluetooth ./sound/RH_0.mp3")
	elif info["RH"] == 1 :
		os.system("mpg123 -a bluetooth ./sound/RH_1.mp3")
	elif info["RH"] == 2 :
		os.system("mpg123 -a bluetooth ./sound/RH_2.mp3")

	if info["RL"] == 0 :
		os.system("mpg123 -a bluetooth ./sound/RL_0.mp3")
	elif info["RL"] == 1 :
		os.system("mpg123 -a bluetooth ./sound/RL_1.mp3")
	elif info["RL"] == 2 :
		os.system("mpg123 -a bluetooth ./sound/RL_2.mp3")

# must to fix
def vibrator_out(info) :
	if info["FH"] == 0 :
		os.system("mpg123 -a bluetooth ./sound/LH_0.mp3")
	elif info["FH"] == 1 :
		os.system("mpg123 -a bluetooth ./sound/LH_1.mp3")
	elif info["FH"] == 2 :
		os.system("mpg123 -a bluetooth ./sound/LH_2.mp3")
	elif info["FL"] == 0 :
		os.system("mpg123 -a bluetooth ./sound/LL_0.mp3")
	elif info["FL"] == 1 :
		os.system("mpg123 -a bluetooth ./sound/LL_1.mp3")
	elif info["FL"] == 2 :
		os.system("mpg123 -a bluetooth ./sound/LL_2.mp3")