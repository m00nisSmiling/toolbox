import requests
import os
from termcolor import colored

print(colored("""

---------------------------------------------------------------------------------
|[GET]--[POST]--[DELETE]--[PATCH]--[PUT]--[HEAD]----------------------> [SERVER]|
---------------------------------------------------------------------------------

""",'magenta'))

input1 = input(colored('METHOD--[get/post/patch/head/delete/put]--->[server] :> ','red'))
input2 = input(colored("URL :> ","blue"))

file1 = open("./wordlists/dir_list.txt").read()
files = file1.splitlines()

log_file = open('log/log.txt','a')
log_file.write(f'[sub] http method dir bruteforcer --> url {input2} --> method {input1}\n')
log_file.close()

headers = {
"Cookie":"a",
"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"
}

if input1 == 'get':
 met_c = colored(input1,'blue')
elif input1 == 'post':
 met_c = colored(input1,'yellow')
elif input1 == 'delete':
 met_c = colored(input1,'red')
elif input1 == 'patch':
 met_c = colored(input1,'cyan')
elif input1 == 'put':
 met_c = colored(input1,'green')
elif input1 == 'head':
 met_c = colored(input1,'red')
 
# get request
if input1=="get":
 for a in files:
  url = f"{input2}{a}"
  req = requests.get(url,headers=headers)
  url_c = colored(url,'blue')
  stat = req.status_code
  if (stat < 300 ):
   b = colored(stat,'blue')
  elif (stat < 400 ):
   b = colored(stat,'yellow')
  elif (stat < 500):
   b = colored(stat,'magenta')
  else:
   b = colored(stat,'red')  

  print(f"[{met_c}]Request To[ {url_c} ] ---> [",b,"]")
  
# post request 
elif input1=="post":
 input_sub = input(colored("Data : ",'yellow'))
 for a in files:
  url = f"{input2}{a}"
  req = requests.post(url,headers=headers,data=input_sub)
  url_c = colored(url,'blue')
  stat = req.status_code
  if (stat < 300 ):
   b = colored(stat,'blue')
  elif (stat < 400 ):
   b = colored(stat,'yellow')
  elif (stat < 500):
   b = colored(stat,'magenta')
  else:
   b = colored(stat,'red') 
  print(f"[{met_c}]Request To[ {url_c} ] ---> [",b,"]")
  
# delete request
elif input1=="delete":
 for a in files:
  url = f"{input2}{a}"
  req = requests.delete(url,headers=headers)
  url_c = colored(url,'blue')
  stat = req.status_code
  if (stat < 300 ):
   b = colored(stat,'blue')
  elif (stat < 400 ):
   b = colored(stat,'yellow')
  elif (stat < 500):
   b = colored(stat,'magenta')
  else:
   b = colored(stat,'red')  

  print(f"[{met_c}]Request To[ {url_c} ] ---> [",b,"]")
  
# patch request
elif input1=="patch":
 for a in files:
  url = f"{input2}{a}"
  req = requests.patch(url,headers=headers)
  url_c = colored(url,'blue')
  stat = req.status_code
  if (stat < 300 ):
   b = colored(stat,'blue')
  elif (stat < 400 ):
   b = colored(stat,'yellow')
  elif (stat < 500):
   b = colored(stat,'magenta')
  else:
   b = colored(stat,'red')  

  print(f"[{met_c}]Request To[ {url_c} ] ---> [",b,"]")

# put request 
elif input1=="put":
 for a in files:
  url = f"{input2}{a}"
  req = requests.put(url,headers=headers)
  url_c = colored(url,'blue')
  stat = req.status_code
  if (stat < 300 ):
   b = colored(stat,'blue')
  elif (stat < 400 ):
   b = colored(stat,'yellow')
  elif (stat < 500):
   b = colored(stat,'magenta')
  else:
   b = colored(stat,'red')  

  print(f"[{met_c}]Request To[ {url_c} ] ---> [",b,"]")

# head request
elif input1=="head":
 inputr = input(colored("Verbose [on/off] :> ",'red'))
 if inputr == 'off':
  for a in files:
   url = f"{input2}{a}"
   req = requests.head(url,headers=headers)
   url_c = colored(url,'blue')
   stat = req.status_code
   if (stat < 300 ):
    b = colored(stat,'blue')
   elif (stat < 400 ):
    b = colored(stat,'yellow')
   elif (stat < 500):
    b = colored(stat,'magenta')
   else:
    b = colored(stat,'red')  
   print(f"[{met_c}]Request To[ {url_c} ] ---> [",b,"]")
 elif inputr == 'on':
  for a in files:
   url = f"{input2}{a}"
   req = requests.head(url,headers=headers)
   url_c = colored(url,'blue')
   stat = req.status_code
   responser = colored(req.headers,'blue')
   if (stat < 300 ):
    b = colored(stat,'blue')
   elif (stat < 400 ):
    b = colored(stat,'yellow')
   elif (stat < 500):
    b = colored(stat,'magenta')
   else:
    b = colored(stat,'red')  
   
   print(f"[{met_c}]Request To[ {url_c} ] ---> [",b,"] Headers[",responser,"]")
