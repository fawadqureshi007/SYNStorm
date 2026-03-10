import os
import sys
import time
import random
from platform import system

# Clear Screen
def clearScr():
    if system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Logo Banner
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    banner = """
███████╗██╗   ██╗███╗   ██╗███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗
██╔════╝╚██╗ ██╔╝████╗  ██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║
███████╗ ╚████╔╝ ██╔██╗ ██║███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║
╚════██║  ╚██╔╝  ██║╚██╗██║╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║
███████║   ██║   ██║ ╚████║███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║
╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝

            SYNStorm - Network Stress Testing Tool

Note: For Educational & Authorized Testing Only

Coded by : Fawad Qureshi
Instagram : h4cker_fawad
Facebook : CipherPhantom
"""

    for line in banner.split("\n"):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.03)

# Menu
def menu():
    print("""
[1] Launch DDOS Tool
[2] Tool Info
[3] Exit
""")

# DDOS launcher
def run_ddos():
    if os.path.exists("files/ddos/ddos.py"):
        if system() == "Windows":
            os.system("cd files\\ddos && python3 ddos.py")
        else:
            os.system("cd files/ddos && chmod +x ddos.py && python3 ddos.py")
    else:
        print("DDOS tool not found!")

# Info
def info():
    print("""
SYNStorm v1.0

A simple CLI tool designed for cybersecurity learners
to understand network stress testing techniques.

Developer : h4cker_fawad
""")
[+] 1. DDOS Tools
			                  """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)						  
        
clearScr()
logo()

luc = input("DDOS@ALEXXX:~# ")
clearScr()

class choices():
    def ddos(self):
        if system() == 'Linux':
            os.system("cd files/ddos && chmod +x ddos.py && python3 ddos.py")
        elif system() == 'Windows':
            os.system('cd files\\ddos && python ddos.py')
        else:
            print("Unsupported OS!")
    
    def exitluc(self):
        print('\033[97m\nClosing Lucille\nPlease Wait...\033[1;m')
        time.sleep(2)
        sys.exit()

ch = choices()
if luc == '1':
    ch.ddos()
elif luc.lower() in ['exit', 'quit', 'q']:
    ch.exitluc()
else:
    print("Invalid Input!")
