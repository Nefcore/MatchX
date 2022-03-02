# -*- coding: utf-8 -*-

# logging outputs

from colorama import Fore as clr, Style
from datetime import datetime

now = datetime.now()
time_now = now.strftime("%d-%m-%Y %H:%M:%S")

cyan = clr.CYAN
green = '\033[92m'
yellow = '\033[93m'
red = clr.RED
bright = Style.BRIGHT
blue = clr.BLUE 
reset = Style.RESET_ALL
Datetime = ("[" + cyan + time_now + reset + "]")

banner = f"""
    __  ___      __       __   _  __
   /  |/  /___ _/ /______/ /_ | |/ /
  / /|_/ / __ `/ __/ ___/ __ \|   / 
 / /  / / /_/ / /_/ /__/ / / /   |  
/_/  /_/\__,_/\__/\___/_/ /_/_/|_|  v1.0

                        ({green}\x1B[3mBy Nefcore\x1B[0m{reset})
"""

def good(msg):
    print(Datetime +" [" + green + bright +'MATCHED' + reset + ']'+msg)

def error(msg):
    print(Datetime +" [" + red + bright +'ERR' + reset + ']',msg)

def info(msg):
    print(Datetime +" [" + blue + 'INF' + reset + "]"+msg)

def warn(msg):
    print(Datetime +" [" + yellow + 'WRN' + reset + "]"+msg)
