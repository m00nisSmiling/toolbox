import requests
from termcolor import colored
import urllib.parse

def rxss():
 #requests.get(f'https://eovzlu8cd49gpu1.m.pipedream.net/?tool=reflectXSS:{list55}')
 print(colored("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

XXXX     XXXX SSSSSSSS SSSSSSSS
  XXXX XXXX   SS       SS
    XXXXX     SSSSSSSS SSSSSSSS
  XXXX XXXX         SS       SS
XXXX     XXXX SSSSSSSS SSSSSSSS

[!] only url parameter reflected xss tester
[!] create a file using one or more multiple reflected endpoints
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""","red"))
 url=input(colored("file [>] ","blue"))
 log_file = open('log/log.txt','a')
 log_file.write(f'[sub] XSS Checker --> url file {url}\n')
 log_file.close()
 print(colored('''
=====================================================================================
                hundred of xssbypass wordlist     -     wordlists.txt
                xss common default wordlist       -     xssbypass.txt
                escape charactor testing wordlist -     escape_test.txt
                            
                             [custom wordlists as you like]
=====================================================================================

''',"red"))
 inpfile = input(colored("wordlist [>] ","blue"))
 if url=='exit':
  os.system('python tool.py')
 else:
  url_file=open(url).read()
  split_url=url_file.splitlines()
  for url_1 in split_url: 
   file1=open(inpfile).read()
   splitk=file1.splitlines()
   for script in splitk:
    req_txt=f"{url_1}{script}"
    req_re=requests.get(req_txt)
    if script in req_re.text:
     print(colored("[ Payload is Reflected Check >>> ] Payload >>","blue"),url_1,script)
    else:
     print(colored("[ Not Found ]","red"))


rxss()
