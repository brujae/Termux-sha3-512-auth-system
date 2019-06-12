import os
import sys
import time
import hashlib
import getpass

#To hash a string go to duckduckgo and type: sha3-512 yourstring
#As echo string | sha3sum -a 512 doesn't seem to work atm.
sha3_512uname = "4d73e85b3f80a06c44fd47540c310019f21d9f5735871297d1789b5821782ede2ddd6c8f79cc65ecccb33b262130547f777e061db05762837dc51e117c0ca4c2" #default username: 73214
sha3_512pword = "c6f22fcae2f30e415f2b7f5efb6c29b959e2b4d1db9fbaf238c63873c7fb44fa9e6709e44cda83bf99fc55deb9dc04aeaaa9de7a9d1646474c1aca87050cd63a" #default password: 1337

#Check if user run it on python < 3
if sys.version_info[0] < 3:
	print("\n\t\tFor \033[31msafety\033[0m it only work on python \033[31m3\033[0m or \033[31mlater.\033[0m\n")
	exit()

def login():
      while True:
           try:
                uname = input('\n\33[34mUsername\033[0m: ')
                pword = getpass.getpass('\33[34mPassword\033[0m: ')
                if hashlib.sha3_512(uname.encode('utf-8')).hexdigest() == sha3_512uname and hashlib.sha3_512(pword.encode('utf-8')).hexdigest() == sha3_512pword:
                   os.system('clear')
                   os.system('printf "Hello "' + uname + '| figlet | lolcat && neofetch') #if you dont like neofetch remove '&& neofetch' 
                   break
                else:
                      print("\n\033[1;91m\t\t\tWrong Password\n\t\t\tTry again.\n")
                      time.sleep(2)
                      os.system('clear')
           except Exception:
                      print("\n\033[1;91m\t\tSomething went wrong?\n")
                      time.sleep(2)
                      os.system('clear')
           except KeyboardInterrupt:
	                  print("\033[1;91m\t\t\tKey not allowed.")
login()
