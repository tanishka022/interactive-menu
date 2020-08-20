import pyttsx3
import os

os.system("color b")

pyttsx3.speak("Welcome to my tools!")

while True:
	print("Enter your choice(chat with me): ", end = '')
	p = input()

	if (("run" in p) or ("execute" in p)) and ("chrome" in p) and (("don't" not in p) and ("not" not in p)):
                os.system("start chrome")

	elif (("run" in p) or ("execute" in p)) and (("power" in p) or ("point" in p) or ("presentation" in p)) and (("don't" not in p) and ("not" not in p)):
    		os.system("powerpnt")

	elif (("run" in p) or ("execute" in p)) and (("calculator" in p) or ("calc" in p)) and (("don't" not in p) and ("not" not in p)):
    		os.system("calc")

	elif (("run" in p) or ("execute" in p)) and (("excel" in p) or ("sheet" in p)) and (("don't" not in p) and ("not" not in p)):
    		os.system("excel")

	elif (("run" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)) and ("don't" not in p):
    		os.system("notepad")

	elif (("run" in p) or ("execute" in p)) and (("player" in p) or ("media" in p)) and (("don't" not in p) and ("not" not in p)):
    		os.system("wmplayer")

	elif (("run" in p) or ("execute" in p)) and ("edge" in p) and (("don't" not in p) and ("not" not in p)):
    		os.system("start microsoftedge")

	elif (("run" in p) or ("execute" in p)) and (("clock" in p) or ("alarm" in p)) and (("don't" not in p) and ("not" not in p)):
    		os.system("start ms-clock:")

	elif (("run" in p) or ("execute" in p)) and (("calendar" in p) or ("outlook" in p)) and (("don't" not in p) and ("not" not in p)):
    		os.system("start outlookcal:")

	elif (("run" in p) or ("execute" in p)) and ("mail" in p) and (("don't" not in p) and ("not" not in p)):
    		os.system("start outlookmail")

	elif (("run" in p) or ("execute" in p)) and ("candy" in p) and (("don't" not in p) and ("not" not in p)):
    		os.system("start candycrushsodasaga:")

	elif ("don't" in p) or ("not" in p):
		print("Okay!")
		os.system("color a")
	
	elif ("exit" in p) or ("quit" in p):
		os.system("color e")
		break

	else:
		os.system("color f")
		print("Doesn't support!")