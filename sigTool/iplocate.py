import requests
from termcolor import colored 

def iplocate():
 #requests.get(f'https://eovzlu8cd49gpu1.m.pipedream.net/?tool=iplocate:{list55}')
 print(colored('''
+++++++++++++++++++++++++++++++++++++++

------- ----
   |    |   )
   |    |---  --- INFO -TRACER
   |    |
_______ |
 
[!] use ip address to get informations 
+++++++++++++++++++++++++++++++++++++++

''','blue'))
 input111 = input(colored('[ip] >> ','red') )

 url = f'https://api.ipgeolocation.io/ipgeo?ip={input111}&apiKey=e6e8fe7cd6ab46c2884c758ec679ba52'
 requestss = requests.get(url)

 if input111 != '':
  print(requestss)
  print(colored('---------------','yellow'))
  print(colored(requestss.text,'white'))
 else:
  print('ERROR!!')
 log_file = open('log/log.txt','a')
 log_file.write(f'[sub] ip info tracer --> ip {input111}\n')
 log_file.close()

iplocate()
