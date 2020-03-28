import time
from termcolor import colored as color
import colorama
from colorama import Fore



print(color("""
╔══╗╔══╗ ╔══╗╔╗╔╗╔════╗
║╔╗║║╔╗║ ║╔╗║║║║║╚═╗╔═╝
║╚╝║║╚╝╚╗║║║║║║║║  ║║
║╔╗║║╔═╗║║║║║║║║║  ║║
║║║║║╚═╝║║╚╝║║╚╝║  ║║
╚╝╚╝╚═══╝╚══╝╚══╝  ╚╝
""","yellow"))
while True:
	time.sleep(0.2)
	print(f"""
{Fore.GREEN}-[1]- How to use?
{Fore.GREEN}-[2]- Authors
{Fore.RED}-[3]- Exit
""")
	ans = input(f"{Fore.RED}[root@user] ==>> {Fore.GREEN}")
	if ans == "2":
		time.sleep(0.5)
		print(f"""
{Fore.CYAN}[1] - Material by Lucifer Pentest Young
[1] - Coded by AviNoire""")
		time.sleep(1)
	elif ans == "3":
		break
	elif ans == "1":
		time.sleep(0.5)
		print(f"""
{Fore.RED}Instuction step by step!
{Fore.CYAN}1) Start VPN
2) Create a bot into @BotFather on Telegram
3) Start bomb.py (python3 bomb.py)
4) Enter bot TOKEN and your Telegram id
5) Go to your bot
6) Start having fun :D
{Fore.RED}~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
		time.sleep(1)
	else:
		time.sleep(0.1)
		print(f"{Fore.RED}---Unknown Command---")
