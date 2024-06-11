import requests
from termcolor import colored
import os

def status():
 #requests.get(f'https://eovzlu8cd49gpu1.m.pipedream.net/?tool=statusChecker:{list55}')
 print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 000000000  00000000 00000000
00       00 00    00 00    00
 00    00   00    00 00    00 <-------OK
     00     00    00 00    00
   00       00    00 00    00
 0000000000 00000000 00000000 

[ input a wordlist that contains multiple urls, ez to use ]

Usage:
STEP1 [ cmd - command mode to create a wordlist(like nano) ]
STEP2 [ on  - input a file(input wordlistname) ]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

''')
 inputw = input("[ on or cmd ? ]: ")
 if inputw=='cmd':
  for i in range(0,100):
   inputcmd=input("$")
   if inputcmd=='on':  
    file11= input("filename in this directory:")
    filew = open(f"{file11}").read()
    filea = filew.splitlines()
    print('--------------------------[200 ok domains]-------------------------------')
    for file in filea:
     checker = f"{file}"
     try:
      requests.get(checker)
     except requests.ConnectionError:
      pass
     else:
      print("[200] ",checker)
   else:
    os.system(inputcmd)
 elif inputw=='on':
  file11= input("filename in this directory:")
  filew = open(f"{file11}").read()
  filea = filew.splitlines()
  print('--------------------------[200 ok domains]-------------------------------')

  for file in filea:
   checker = f"{file}"
   try:
    requests.get(checker)
   except requests.ConnectionError:
    pass
   else:
    print(checker)
 log_file = open('log/log.txt','a')
 log_file.write(f'[sub] status checker --> url file name {file11}\n')
 log_file.close()

status()
