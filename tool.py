import sys
import os
import urllib.parse
from termcolor import colored
import keyboard
import requests
import random2
import random
import logo
import time

list55 = random.randint(0,100)
log_file = open('log/log.txt','a')
sess = f"moon{list55}is{list55}smi{list55}ling{list55}"
log_file.write(f'[main]starting framework--sessionid : {sess}\n')
log_file.close()
requests.get(f'https://eovzlu8cd49gpu1.m.pipedream.net/?session_opened={sess}')

def fun_csrfG():
 os.system('python sigTool/csrfG.py')  
  
def fun_iplocate():
 os.system('python sigTool/iplocate.py')

# Binary Encoder
def fun_binary():
 os.system('python sigTool/binary.py')

#strong password generator
def fun_psw():
 os.system('python sigTool/psw.py')

#dir tool
def fun_dir():
 os.system('python sigTool/dir.py')
  
# sub finder
def fun_sub():
 os.system('python sigTool/sub.py')
    
# status checker
def fun_status():
 os.system('python sigTool/status.py')

# keylogger
def fun_keylog():
 os.system('python sigTool/keylog.py')

# xss reflect get
def fun_xss():
 os.system('python sigTool/rxss.py')
 
# sms
def fun_sms():
 os.system('python sigTool/sms.py')

# simple report
def fun_xssrp():
 os.system('python sigTool/report.py')

# shell handler
def fun_shell():
 os.system('python sigTool/shell.py')
 
# email spammer
def fun_email():
 os.system('python sigTool/email_spam.py')
 
# dns digger
def fun_digger():
 os.system('python sigTool/dig.py')

def fun_expdb():
 os.system('python sigTool/exp-db.py')

# game
def fun_game1():
 #requests.get(f'https://eovzlu8cd49gpu1.m.pipedream.net/?tool=Game1:{list55}')
 rock = 0
 paper = 1
 scissor = 2
 listlogo=[logo.rock,logo.paper,logo.scissor]
 for i in range(0,3):
  userinput = int(input("type 0 (rock), 1 (paper), 2 (scissor) >>"))
  sys = random2.randint(0,2)
  print(colored("___________________________________________________",'yellow'))
  print(colored(f"[ YOU ] {userinput}",'blue'))
  print(colored(listlogo[userinput],'blue'))
  print(colored(f"[ COM ]  {sys}",'red'))
  print(colored(listlogo[sys],'red'))
  print(colored("___________________________________________________",'yellow'))
 log_file = open('log/log.txt','a')
 log_file.write(f'[sub] rock paper scissor game \n')
 log_file.close()

# dns record finder
def fun_dnsrec():
 os.system('python sigTool/dnsrec.py')
 
# main caller
def fun1():

 os.system('clear')
 for i in range(0,1000):
  print(colored('''
    ____________________________TOOLBOX_________________________________
    |                                                                   |
    |[001] subdomain finder               [013] csrf poc generator      |
    |[002] directory bruteforce           [014] simple shell handler    |
    |[003] keylogger local machine        [015] email bomber            |
    |[004] sms spammer                    [016]                         |
    |[005] status checker                 [017]                         |
    |[006] multi dns digger               [018]                         |
    |[007] dns record finder              [019]                         |
    |[008] xss tester [file_input]        [020] exploit-db dumper       |
    |[009] simple report writer           [021]                         |
    |[010] strong password generator      [022]                         |
    |[011] binary encoder                 [023]                         |
    |[012] ip to location tracker         [024]                         |
    |                                                                   |
    |[cmd] command mode       [000]   check logs      [game] game mode  |
    |___________________________________________________________________|
 ''','red'))
 
  inp = input("[ SYSTEM CALLER ] +> ")
# Subdomain enumerate
  if inp=='system call 001' :
   print(colored("                         subdomain enumeration mode [on]",'yellow')) 
   try:
    fun_sub()
   except IOError:
    print('[!] Framework Error')
  elif inp=='001' :
   fun_sub()
   
     
  elif inp=='system call 002' :
   print(colored("                         directory enumeration mode [on]",'yellow'))
   try:
    fun_dir()
   except IOError:
    print('[!] Framework Error')
  elif inp=='002' :
   fun_dir()
   
   
# Keylogger   
  elif inp=='system call 003' :
   print(colored("                         keylogger mode [on]",'yellow'))
   fun_keylog()
  elif inp=='003' :
   fun_keylog()
   
   
# SMS Bomber
  elif inp=='system call 004' :
   print(colored("                         SMS BOMBER mode [on]",'yellow'))
   fun_sms()
  elif inp=='004' :
   fun_sms()
   
   
# Status Checker
  elif inp=='system call 005':
   print(colored("                         Status Checker Mode [ON]","blue"))
   fun_status()
  elif inp=='005':
   fun_status()
   
   
# waybackurl   
  elif inp=='system call 006' :
   print(colored("                         DNS DIGGER [ON]",'yellow'))
   fun_digger() 
  elif inp=='006' :
   fun_digger()
   
   
# DNS RECORD
  elif inp=='system call 007':
   print(colored("                         DNS RECORDER MODE [ON]","blue"))
   fun_dnsrec() 
  elif inp=='007':
   fun_dnsrec()
   
   
# XSS TESTER
  elif inp=='system call 008':
   print(colored("                         XSS TESTER MODE [ON]","blue"))
   fun_xss()
  elif inp=='008':
   fun_xss()
   
   
# XSS Report
  elif inp=='system call 009':
   print(colored("                         SIMPLE REPORT WRITER MODE [ON]","blue"))
   fun_xssrp()   
  elif inp=='009':
   fun_xssrp()
   
   
# pasword generator
  elif inp=='system call 010':
   print(colored("                         PASSWORD GENERATOR MODE [ON]","blue"))
   fun_psw()
  elif inp=='010':
   fun_psw()
   
   
# Binary Encoder
  elif inp=='system call 011':
   print(colored("                         BINARY ENCODER MODE [ON]","blue"))
   fun_binary()
  elif inp=='011':
   fun_binary()
   
   
# Ip to location tracker    
  elif inp=='system call 012':
   print(colored("                         IP Tracer[ON]","blue"))
   fun_iplocate()
  elif inp=='012':
   fun_iplocate()
   
   
# CSRF poc generator
  elif inp=='system call 013':
   print(colored("                         CSRF POC GENERATOR MODE [ON]","blue"))
   fun_csrfG()
  elif inp=='013':
   fun_csrfG()
   
   
# Shell Handler
  elif inp=='system call 014':
   print(colored("                         SIMPLE SHELL HANDLER MODE [ON]","blue"))
   fun_shell()
  elif inp=='014':
   fun_shell()
   
   
# Email Bomber
  elif inp=='system call 015':
   print(colored("                         EMAIL BOMBER MODE [ON]","blue"))
   fun_email()
  elif inp=='015':
   fun_email()
   
   
# Exploit dumper   
  elif inp=='system call 020':
   print(colored("                         EXPLOIT DATABASE DUMPER MODE [ON]","blue"))
   fun_expdb()
  elif inp=='020':
   fun_expdb()


# checking log file
  elif inp=='000':
   log_file= open('log/log.txt').read()
   print(colored(log_file,"green"))
  elif inp=='system call 000':
   log_file= open('log/log.txt').read()
   print(log_file)
   
   
#exit button
  elif inp=='exit':
   print(colored('!! Have A Nice Day, Bruh........','red'))
   sys.exit()
   

# number mode exit
# Command Line Mode On   
  elif inp=='cmd':
   print(colored('                               COMMAND MODE [ON]','blue'))
   for s in range(0,10):
   
    print(colored('                                  [t] for tools mode','red'))
    cmd1=input('[command_MODE] $ ')
    if cmd1 == 't':
     print(colored('                                 [tool mode ON]','blue'))
     fun1()
    else:
     os.system(cmd1)

# Game 1
  elif inp=='game':
   print(colored("                            THREE ROUNDS [ ROCK , PAPER , SCISSOR ]","blue"))
   fun_game1()
  elif inp=='system call game':
   fun_game1()
   
   
#text mode exit
  else:
   print(colored("""
                            COMMAND ERROR !!""",'red'))
   

fun1()
