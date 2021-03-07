import requests
import random
import string
from requests.auth import HTTPProxyAuth
import time
import threading
from itertools import cycle
import json
from colorama import Fore
import os
os.system('color')


with open('config.json', 'r') as jsonfile:
    data = json.load(jsonfile)
channelid = data['channelid']
def SendBeg():
    try:
        print(f"{Fore.GREEN}[ + ] Sent: pls beg{Fore.RESET}")
        currmessage = 'pls beg'
        requests.post(f'https://discord.com/api/v8/channels/{channelid}/messages',
                                    headers={'authorization': data['token']},
                                    data={'content': currmessage})
    except Exception as err:
        print(err)
def SendPM():
    try:
        print(f"{Fore.GREEN}[ + ] Sent: pls pm{Fore.RESET}")
        currmessage = 'pls pm'
        requests.post(f'https://discord.com/api/v8/channels/{channelid}/messages',
                                    headers={'authorization': data['token']},
                                    data={'content': currmessage})
        time.sleep(2)
        currmessage = 'f'
        requests.post(f'https://discord.com/api/v8/channels/{channelid}/messages',
                                    headers={
                                        'authorization': data['token']},
                                    data={'content': currmessage})
    except Exception as err:
        print(err)
def SendFish():
    try:
        print(f"{Fore.GREEN}[ + ] Sent: pls fish{Fore.RESET}")
        currmessage = 'pls fish'
        requests.post(f'https://discord.com/api/v8/channels/{channelid}/messages',
                                    headers={'authorization': data['token']},
                                    data={'content': currmessage})
    except Exception as err:
        print(err)
def SendHunt():
    try:
        print(f"{Fore.GREEN}[ + ] Sent: pls hunt{Fore.RESET}")
        currmessage = 'pls hunt'
        requests.post(f'https://discord.com/api/v8/channels/{channelid}/messages',
                                    headers={'authorization': data['token']},
                                    data={'content': currmessage})
    except Exception as err:
        print(err)
def MainFunc():
    while True:
        SendBeg()
        time.sleep(2)
        SendPM()
        time.sleep(2)
        SendFish()
        time.sleep(2)
        SendHunt()
        time.sleep(54)



print(f"""{Fore.BLUE}
+-----+--------------------------+
|##| Tool List and Versions      |
+-----+--------------------------|
|  1  | DankMeme autofarm - 0.4.3|
+--------------------------------+


""")
choice = input('>>>> ' + Fore.RESET)

if choice == '1':
    MainFunc()
