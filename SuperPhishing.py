#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os
import sys
import time
from colorama import Fore, Style

#Referencias
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'

os.system("clear")

def banner():
	print('''
    
  \033[1;36m<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\033[0;m
  \033[1;36m<>\033[0;m                                                              \033[1;36m<>\033[0;m
  \033[1;36m<>\033[0;m           ███████╗██╗   ██╗██████╗ ███████╗██████╗           \033[1;36m<>\033[0;m
  \033[1;36m<>\033[0;m           ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗          \033[1;36m<>\033[0;m
  \033[1;36m<>\033[0;m           ███████╗██║   ██║██████╔╝█████╗  ██████╔╝          \033[1;36m<>\033[0;m
  \033[1;36m<>\033[0;m           ╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗          \033[1;36m<>\033[0;m
  \033[1;36m<>\033[0;m           ███████║╚██████╔╝██║     ███████╗██║  ██║          \033[1;36m<>\033[0;m
  \033[1;36m<>\033[0;m           ╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝          \033[1;36m<>\033[0;m
  \033[1;36m<>\033[0;m                                                              \033[1;36m<>\033[0;m
  \033[1;36m<>\033[0;m                                                              \033[1;36m<>\033[0;m                           
  \033[1;36m<>\033[0;m  \033[0;31m  ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗\033[0;m  \033[1;36m<>\033[0;m
  \033[1;36m<>\033[0;m  \033[0;31m  ██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝\033[0;m  \033[1;36m<>\033[0;m
  \033[1;36m<>\033[0;m  \033[0;31m  ██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗\033[0;m \033[1;36m<>\033[0;m
  \033[1;36m<>\033[0;m  \033[0;31m  ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║\033[0;m \033[1;36m<>\033[0;m
  \033[1;36m<>\033[0;m  \033[0;31m  ██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝\033[0;m \033[1;36m<>\033[0;m
  \033[1;36m<>\033[0;m  \033[0;31m  ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ \033[0;m \033[1;36m<>\033[0;m
  \033[1;36m<>\033[0;m                                                              \033[1;36m<>\033[0;m 
  \033[1;36m<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\033[0;m                                                       
                    \033[1;34m----<\033[0;m \033[1;44;37mCREADOR: R3LI4NT\033[0;m \033[1;34m>----\033[0;m                                            
                                               
              \033[1;32m----<\033[0;m \033[1;42;37mKIT DE HERRAMIENTAS PHISHING\033[0;m \033[1;32m>----\033[0;m                                             
                                             
                      \033[1;31m----<\033[0;m \033[1;41;37mVERSION: 1.0\033[0;m \033[1;31m>----\033[0;m                                             
''')
banner()


def Wait():
	print(BLUE + Style.BRIGHT+"""
   __          __   _ _         
   \ \        / /  (_) |        
    \ \  /\  / /_ _ _| |_       
     \ \/  \/ / _` | | __|      
      \  /\  / (_| | | |_ _ _ _ 
       \/  \/ \__,_|_|\__(_|_|_)
                                                            
"""+ WHITE + Style.NORMAL)


def GoodBye():
	print("""
   \033[1;37m   ______                ______            \033[0;m
   \033[1;37m  / ____/___  ____  ____/ / __ )__  _____  \033[0;m
   \033[1;37m / / __/ __ \/ __ \/ __  / __  / / / / _ \ \033[0;m
   \033[1;37m/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/ \033[0;m
   \033[1;37m\____/\____/\____/\__,_/_____/\__, /\___/  \033[0;m
   \033[1;37m                             /____/        \033[0;m
                          \033[1;31m     ______     _                ____   \033[0;m
                          \033[1;31m    / ____/____(_)__  ____  ____/ / /   \033[0;m
                          \033[1;31m   / /_  / ___/ / _ \/ __ \/ __  / /    \033[0;m
                          \033[1;31m  / __/ / /  / /  __/ / / / /_/ /_/     \033[0;m
                          \033[1;31m /_/   /_/  /_/\___/_/ /_/\__,_(_)      \033[0;m                                                       
""")


time.sleep(0.5)                                             

if input("\033[1;41;37mADVERTENCIA\033[0;m \033[1;33m¿Acepta utilizar esta herramienta con fines educativos?\033[0;m [\033[1;32my\033[0;m / \033[1;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
    os.system('clear') 
    print("\n\n\033[1;42;37mGOODBYE\033[0;m \033[1;31mLo siento, no puedo permitirte el acceso :P\033[0;m\n\n")
    time.sleep(0.8)
    exit(0)


os.system("clear")
banner()


def menu():
	print("""[\033[0;31m01\033[0;m] \033[1;36mHiddenEye\033[0;m     [\033[0;31m06\033[0;m] \033[1;36mSocialFish\033[0;m
[\033[0;31m02\033[0;m] \033[1;36mZphisher\033[0;m      [\033[0;31m07\033[0;m] \033[1;36mAdvPhishing\033[0;m
[\033[0;31m03\033[0;m] \033[1;36mBlackPhish\033[0;m    [\033[0;31m08\033[0;m] \033[1;36mBlackEye\033[0;m
[\033[0;31m04\033[0;m] \033[1;36mShellphish\033[0;m    [\033[0;31m09\033[0;m[ \033[1;36mShark\033[0;m
[\033[0;31m05\033[0;m] \033[1;36mPhisherman\033[0;m    [\033[0;32m00\033[0;m] \033[0;31mExit\033[0;m
""")
menu()

X = input("\033[1;37m>>\033[0;m ")

if X == "01":
    Wait()
    tool = os.system("clear")
    Wait()
    tool = print("\033[1;33mClonando repositorio...\033[0;m\n")
    tool = os.system("git clone https://github.com/DarkSecDevelopers/HiddenEye-Legacy")
    tool = time.sleep(0.9)
    tool = print("\n\033[1;33mCompletado!\033[0;m\n")
    if input("\033[1;37m¿Ejecutar herramienta?\033[0;m \033[0;m[\033[1;32my\033[0;m / \033[1;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
    	os.system("clear")
    	GoodBye()
    	print("\n\033[1;32mGracias por usar este script, vuelve nuevamente!\n\033[0;m\n")
    	exit(0)

    tool = os.system("clear")
    tool = print("""

      \033[1;34m<---------------------->\033[0;m 
            \033[1;34mEJECUTANDO...\033[0;m
      \033[1;34m<---------------------->\033[0;m    
      """)
    tool = time.sleep(0.5)    
    tool = os.system("cd HiddenEye-Legacy && sudo pip install -r requirements.txt && chmod +x HiddenEye.py && python3 HiddenEye.py")	
	

elif X == "02":
    Wait()
    tool = os.system("clear")
    Wait()
    tool = print("\033[1;33mClonando repositorio...\033[0;m\n")
    tool = os.system("git clone https://github.com/htr-tech/zphisher")
    tool = time.sleep(0.9)
    tool = print("\n\033[1;33mCompletado!\033[0;m\n")
    if input("\033[1;37m¿Ejecutar herramienta?\033[0;m \033[0;m[\033[1;32my\033[0;m / \033[1;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
    	os.system("clear")
    	GoodBye()
    	print("\n\033[1;32mGracias por usar este script, vuelve nuevamente!\n\033[0;m\n")
    	exit(0)
    
    tool = os.system("clear")
    tool = print("""

      \033[1;34m<---------------------->\033[0;m 
            \033[1;34mEJECUTANDO...\033[0;m
      \033[1;34m<---------------------->\033[0;m    
      """)
    tool = time.sleep(0.5)
    tool = os.system("cd zphisher && bash zphisher.sh")


elif X == "03":
    Wait()
    tool = os.system("clear")
    Wait()
    tool = print("\033[1;33mClonando repositorio...\033[0;m\n")
    tool = os.system("git clone https://github.com/iinc0gnit0/BlackPhish")
    tool = time.sleep(0.9)
    tool = print("\n\033[1;33mCompletado!\033[0;m\n")
    if input("\033[1;37m¿Ejecutar herramienta?\033[0;m \033[0;m[\033[1;32my\033[0;m / \033[1;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
    	os.system("clear")
    	GoodBye()
    	print("\n\033[1;32mGracias por usar este script, vuelve nuevamente!\n\033[0;m\n")
    	exit(0)

    tool = os.system("clear")
    tool = print("""

      \033[1;34m<---------------------->\033[0;m 
            \033[1;34mEJECUTANDO...\033[0;m
      \033[1;34m<---------------------->\033[0;m    
      """)
    tool = time.sleep(0.5)
    tool = os.system("cd BlackPhish && ./install.sh && sudo python3 blackphish.py")	    	


elif X == "04":
    Wait()
    tool = os.system("clear")
    Wait()
    tool = print("\033[1;33mClonando repositorio...\033[0;m\n")
    tool = os.system("git clone https://github.com/suljot/shellphish")
    tool = time.sleep(0.9)
    tool = print("\n\033[1;33mCompletado!\033[0;m\n")
    if input("\033[1;37m¿Ejecutar herramienta?\033[0;m \033[0;m[\033[1;32my\033[0;m / \033[1;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
    	os.system("clear")
    	GoodBye()
    	print("\n\033[1;32mGracias por usar este script, vuelve nuevamente!\n\033[0;m\n")
    	exit(0)

    tool = os.system("clear")
    tool = print("""

      \033[1;34m<---------------------->\033[0;m 
            \033[1;34mEJECUTANDO...\033[0;m
      \033[1;34m<---------------------->\033[0;m    
      """)
    tool = time.sleep(0.5)
    tool = os.system("cd shellphish && bash shellphish.sh")	    	


elif X == "05":
    Wait()
    tool = os.system("clear")
    Wait()
    tool = print("\033[1;33mClonando repositorio...\033[0;m\n")
    tool = os.system("git clone https://github.com/FDX100/Phisher-man")
    tool = time.sleep(0.9)
    tool = print("\n\033[1;33mCompletado!\033[0;m\n")
    if input("\033[1;37m¿Ejecutar herramienta?\033[0;m \033[0;m[\033[1;32my\033[0;m / \033[1;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
    	os.system("clear")
    	GoodBye()
    	print("\n\033[1;32mGracias por usar este script, vuelve nuevamente!\n\033[0;m\n")
    	exit(0)

    tool = os.system("clear")
    tool = print("""

      \033[1;34m<---------------------->\033[0;m 
            \033[1;34mEJECUTANDO...\033[0;m
      \033[1;34m<---------------------->\033[0;m    
      """)
    tool = time.sleep(0.5)
    tool = os.system("cd Phisher-man && python phisherman.py")


elif X == "06":
    Wait()
    tool = os.system("clear")
    Wait()
    tool = print("\033[1;33mClonando repositorio...\033[0;m\n")
    tool = os.system("git clone https://github.com/UndeadSec/SocialFish")
    tool = time.sleep(0.9)
    tool = print("\n\033[1;33mCompletado!\033[0;m\n")
    if input("\033[1;37m¿Ejecutar herramienta?\033[0;m \033[0;m[\033[1;32my\033[0;m / \033[1;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
    	os.system("clear")
    	GoodBye()
    	print("\n\033[1;32mGracias por usar este script, vuelve nuevamente!\n\033[0;m\n")
    	exit(0)

    tool = os.system("clear")
    tool = print("""

      \033[1;34m<---------------------->\033[0;m 
            \033[1;34mEJECUTANDO...\033[0;m
      \033[1;34m<---------------------->\033[0;m    
      """)
    tool = time.sleep(0.5)
    tool = os.system("cd SocialFish && sudo pip install -r requirements.txt && python3 SocialFish.py myusername 1234")


elif X == "07":
    Wait()
    tool = os.system("clear")
    Wait()
    tool = print("\033[1;33mClonando repositorio...\033[0;m\n")
    tool = os.system("git clone https://github.com/Ignitetch/AdvPhishing")
    tool = time.sleep(0.9)
    tool = print("\n\033[1;33mCompletado!\033[0;m\n")
    if input("\033[1;37m¿Ejecutar herramienta?\033[0;m \033[0;m[\033[1;32my\033[0;m / \033[1;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
    	os.system("clear")
    	GoodBye()
    	print("\n\033[1;32mGracias por usar este script, vuelve nuevamente!\n\033[0;m\n")
    	exit(0)

    tool = os.system("clear")
    tool = print("""

      \033[1;34m<---------------------->\033[0;m 
            \033[1;34mEJECUTANDO...\033[0;m
      \033[1;34m<---------------------->\033[0;m    
      """)
    tool = time.sleep(0.5)
    tool = os.system("cd AdvPhishing && chmod 777 * && ./Linux-Setup.sh && ./AdvPhishing.sh")


elif X == "08":
    Wait()
    tool = os.system("clear")
    Wait()
    tool = print("\033[1;33mClonando repositorio...\033[0;m\n")
    tool = os.system("git clone https://github.com/An0nUD4Y/blackeye")
    tool = time.sleep(0.9)
    tool = print("\n\033[1;33mCompletado!\033[0;m\n")
    if input("\033[1;37m¿Ejecutar herramienta?\033[0;m \033[0;m[\033[1;32my\033[0;m / \033[1;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
    	os.system("clear")
    	GoodBye()
    	print("\n\033[1;32mGracias por usar este script, vuelve nuevamente!\n\033[0;m\n")
    	exit(0)

    tool = os.system("clear")
    tool = print("""

      \033[1;34m<---------------------->\033[0;m 
            \033[1;34mEJECUTANDO...\033[0;m
      \033[1;34m<---------------------->\033[0;m    
      """)
    tool = time.sleep(0.5)
    tool = os.system("cd blackeye && bash blackeye.sh")    


elif X == "09":
    Wait()
    tool = os.system("clear")
    Wait()
    tool = print("\033[1;33mClonando repositorio...\033[0;m\n")
    tool = os.system("git clone https://github.com/bhikandeshmukh/shark")
    tool = time.sleep(0.9)
    tool = print("\n\033[1;33mCompletado!\033[0;m\n")
    if input("\033[1;37m¿Ejecutar herramienta?\033[0;m \033[0;m[\033[1;32my\033[0;m / \033[1;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
    	os.system("clear")
    	GoodBye()
    	print("\n\033[1;32mGracias por usar este script, vuelve nuevamente!\n\033[0;m\n")
    	exit(0)

    tool = os.system("clear")
    tool = print("""

      \033[1;34m<---------------------->\033[0;m 
            \033[1;34mEJECUTANDO...\033[0;m
      \033[1;34m<---------------------->\033[0;m    
      """)
    tool = time.sleep(0.5)
    tool = os.system("cd shark && chmod +x * && ./kali-setup && shark")


elif X == "00":
    tool = os.system("clear")
    GoodBye()
    print("\n\033[1;32mGracias por usar este script, vuelve nuevamente!\n\033[0;m\n")
    exit(0)

# END OF CODE :)             