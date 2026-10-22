import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

import os, sys

# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        pass

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()


# Initial setup and promotion
os.system('clear')
print(' \x1b[38;5;46m𝐙𝐈𝐘𝐀  𝐒𝐄𝐑𝐕𝐄𝐑 𝐋𝐎𝐀𝐃𝐈𝐍𝐆....')
print('loading Modules ...\n')
os.system('clear')

# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m' 

# ==================== BANNER COLORS ====================
RESET  = '\033[0m'
BOLD   = '\033[1m'

RED    = '\033[38;5;196m'
ORANGE = '\033[38;5;208m'
YELLOW = '\033[38;5;226m'
GREEN  = '\033[38;5;46m'
CYAN   = '\033[38;5;51m'
BLUE   = '\033[38;5;39m'
PURPLE = '\033[38;5;129m'
PINK   = '\033[38;5;201m'
WHITE  = '\033[1;37m'
GRAY   = '\033[38;5;245m'

R = RR
P = PP
C = GS
RESET = W

def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = "Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]"
    return "Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]"


def window1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])


# Set window title
sys.stdout.write('\x1b]2;𓆩【👑𝐙𝐈𝐘𝐀👑 】𓆪 \x07')


def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    
    print("""\033[1;32m
  
███████╗██╗██╗   ██╗ █████╗ 
╚══███╔╝██║╚██╗ ██╔╝██╔══██╗
  ███╔╝ ██║ ╚████╔╝ ███████║
 ███╔╝  ██║  ╚██╔╝  ██╔══██║
███████╗██║   ██║   ██║  ██║
╚══════╝╚═╝   ╚═╝   ╚═╝  ╚═╝
                                                      
\033[1;35m[+]𝐆𝐇𝐀𝐘𝐀𝐋 𝐓𝐎 𝐘𝐀𝐇𝐀 𝐇𝐀𝐑 𝐏𝐀𝐑𝐈𝐍𝐃𝐀 𝐇𝐀𝐈 𝐌𝐀𝐆𝐀𝐑")   
 \033[1;32m----------------------------------------------                           
 \033[1;32m[+] 𝐎𝐖𝐍𝐄𝐑  :       𝐙𝐈𝐘𝐀💞𝐏𝐈𝐈𝐄           💞🅛︎🅞︎ⓥⓔ💞
 \033[1;33m[+] 𝐁𝐄𝐒𝐓𝐈𝐄 :       𝐒𝐇𝐈𝐅𝐔💞 𝐏𝐈𝐈𝐄     ….. (¯`v´¯)♥
 \033[1;33m[+] 𝐁𝐄𝐒𝐓𝐔  :       𝐑𝐈𝙙𝙙𝐔💞𝐁𝐀𝐁𝐔    🫨…….•.¸.•´💞
 \033[1;33m[+] 𝐓𝐎𝐎𝐋𝐒  :       𝐅𝐁💞𝐎𝐋𝐃💋𝐂𝐋𝐎𝐍𝐈𝐂🫨….¸.•´💞
 \033[1;33m[+] 𝐒𝐓𝐀𝐓𝐔𝐒 :       𝐅𝐑𝐄𝐄👀𝐀𝐏𝐑𝐎𝐕𝐄𝐋🫨… (♡💞
  \033[1;32m----------------------------------------------
\033[1;35m[+]𝐉𝐎 𝐅𝐈𝐑  𝐒𝐄 𝐔𝐃 𝐒𝐀𝐊𝐄 𝐖𝐀𝐇𝐈 𝐙𝐈𝐍𝐃𝐀 𝐇𝐀𝐈 𝐙𝐀𝐍𝐀𝐁𝐁""")

#-----------------------( LOOP )-----------------------#
loop=0
tl=0
ok_count=0
cp_count=0
dones=[]
oks=[]
cps=[]
nov=[]
kitty=[]
nvs=[]
twf=[]
gen=[]
plist=[]
__COOKIE__=[]
__CP__=[]
__LOCK__=[]

#-----------------------( MAIN/MENU )-----------------------#
def __MENU__():      
    print("1. AUTO CREATE FB")
    print("2. 2FA")
    print("3. COOKIE EXTRACT")
    print("0. EXIT TOOLS")
    linex()
    __MENUC__=input("INPUT MENU : ")
    if __MENUC__=="1":
       __AUTOX__()
    elif __MENUC__=="2":
       __2FAX__()
    elif __MENUC__=="3":
       __COKIX__()
    elif __MENUC__=="0":
       linex(); print("EXIT SUCCESSFULLY "); time.sleep(1.1); linex(); sys.exit()
    else:
       linex(); print("INVALID OPTION TRY AGAIN "); time.sleep(1); __MENU__()

#-----------------------( AUTO-MENU )-----------------------#
def __AUTOX__(*args, **kwargs):
    print(f"\n{G}AUTO FEATURE IS RUNNING...{W}")
    time.sleep(2)

#-----------------------( 2FA-MENU )-----------------------#
def __2FAX__():
    print("COMING SOON")
    exit()

#-----------------------( COKI-MENU )-----------------------#
def __COKIX__():
    print("COMING SOON")
    exit()

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith(('1000000000', '100000000', '10000000')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''

def clear():
    os.system('clear')

def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def BNG_71_():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD ACCOUNT TOOL')
    linex()
    __Jihad__ = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;41mCHOICE  {W}: {Y}")
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()

def old_clone(*args, **kwargs):
    print(f"\n{G}OLD CLONING TOOL IS RUNNING SUCCESSFULLY...{W}")
    time.sleep(2)
    __MENU__()

if __name__ == '__main__':
    BNG_71_()
