import requests
import os
from termcolor import colored

print(colored("""

---------------------------------------------------------------------------------
|[GET]--[POST]--[DELETE]--[PATCH]--[PUT]--[HEAD]--[ALL]----------------------> [SERVER]|
---------------------------------------------------------------------------------

""",'magenta'))

input1 = input(colored('METHOD--[get/post/patch/head/delete/put]--[all]--->[server] :> ','red'))
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
  # file writing condition state
  if (stat < 400 or stat > 499):
   af = open('./log/METHOD_RESULTS.txt','a')
   ah = af.write(f"[{met_c}]To[ {url_c} ] > [{b}]\n")
   af.close()
  else:
   pass
  print(f"[{met_c}]To[ {url_c} ] > [",b,"]")
  
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
  # file writing condition state
  if (stat < 400 or stat > 499):
   af = open('./log/METHOD_RESULTS.txt','a')
   ah = af.write(f"[{met_c}]To[ {url_c} ] > [{b}]\n")
   af.close()
  else:
   pass
  print(f"[{met_c}]To[ {url_c} ] > [",b,"]")
  
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
  # file writing condition state
  if (stat < 400 or stat > 499):
   af = open('./log/METHOD_RESULTS.txt','a')
   ah = af.write(f"[{met_c}]To[ {url_c} ] > [{b}]\n")
   af.close()
  else:
   pass
  print(f"[{met_c}]To[ {url_c} ] > [",b,"]")
  
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
  # file writing condition state
  if (stat < 400 or stat > 499):
   af = open('./log/METHOD_RESULTS.txt','a')
   ah = af.write(f"[{met_c}]To[ {url_c} ] > [{b}]\n")
   af.close()
  else:
   pass
  print(f"[{met_c}]To[ {url_c} ] > [",b,"]")

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
  # file writing condition state
  if (stat < 400 or stat > 499):
   af = open('./log/METHOD_RESULTS.txt','a')
   ah = af.write(f"[{met_c}]To[ {url_c} ] > [{b}]\n")
   af.close()
  else:
   pass
  print(f"[{met_c}]To[ {url_c} ] > [",b,"]")

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
   print(f"[{met_c}]To[ {url_c} ] > [",b,"]")
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
   # file writing condition state
   if (stat < 400 or stat > 499):
    af = open('./log/METHOD_RESULTS.txt','a')
    ah = af.write(f"[{met_c}]To[ {url_c} ] > [{b}]\n")
    af.close()
   else:
    pass
   print(f"[{met_c}]To[ {url_c} ] > [",b,"] Headers[",responser,"]")
   

# all request methods 
else:
  for a in files:
   met1 = colored("get","blue")
   met2 = colored("post","yellow")
   met3 = colored("delete","red")
   met4 = colored("patch","cyan")
   met5 = colored("put","green")
   met6 = colored("head","red")
   
   # get
   url = f"{input2}{a}"
   url_c = colored(url,'blue')
   
   req1 = requests.get(url,headers=headers)
   stat1 = req1.status_code
   if (stat1 < 300 ):
    b1 = colored(stat1,'blue')
   elif (stat1 < 400 ):
    b1 = colored(stat1,'yellow')
   elif (stat1 < 500):
    b1 = colored(stat1,'magenta')
   else:
    b1 = colored(stat1,'red')  
   print(f"[{met1}]To[ {url_c} ] > [",b1,"]")
   if (stat1 < 400 or stat1 > 499):
    af = open('./log/METHOD_RESULTS.txt','a')
    ah = af.write(f"[{met1}]To[ {url_c} ] > [{b1}]\n")
    af.close()
   else:
    pass
    
   # post
   req2 = requests.post(url,headers=headers)
   stat2 = req2.status_code
   if (stat2< 300 ):
    b2 = colored(stat2,'blue')
   elif (stat2 < 400 ):
    b2 = colored(stat2,'yellow')
   elif (stat2 < 500):
    b2 = colored(stat2,'magenta')
   else:
    b2 = colored(stat2,'red')
   print(f"[{met2}]To[ {url_c} ] > [",b2,"]")
   if (stat2 < 400 or stat2 > 499):
    af = open('./log/METHOD_RESULTS.txt','a')
    ah = af.write(f"[{met2}]To[ {url_c} ] > [{b2}]\n")
    af.close()
   else:
    pass
    
   # delete
   req3 = requests.delete(url,headers=headers)
   stat3 = req3.status_code
   if (stat3 < 300 ):
    b3 = colored(stat3,'blue')
   elif (stat3 < 400 ):
    b3 = colored(stat3,'yellow')
   elif (stat3 < 500):
    b3 = colored(stat3,'magenta')
   else:
    b3 = colored(stat3,'red')    
   print(f"[{met3}]To[ {url_c} ] > [",b3,"]")   
   if (stat3 < 400 or stat3 > 499):
    af = open('./log/METHOD_RESULTS.txt','a')
    ah = af.write(f"[{met3}]To[ {url_c} ] > [{b3}]\n")
    af.close()
   else:
    pass
   
   # patch
   req4 = requests.patch(url,headers=headers)
   stat4 = req4.status_code   
   if (stat4 < 300 ):
    b4 = colored(stat4,'blue')
   elif (stat4 < 400 ):
    b4 = colored(stat4,'yellow')
   elif (stat4 < 500):
    b4 = colored(stat4,'magenta')
   else:
    b4 = colored(stat4,'red') 
   print(f"[{met4}]To[ {url_c} ] > [",b4,"]")
   if (stat4 < 400 or stat4 > 499):
    af = open('./log/METHOD_RESULTS.txt','a')
    ah = af.write(f"[{met4}]To[ {url_c} ] > [{b4}]\n")
    af.close()
   else:
    pass
   
   # put
   req5 = requests.put(url,headers=headers)
   stat5 = req5.status_code
   if (stat5 < 300 ):
    b5 = colored(stat5,'blue')
   elif (stat5 < 400 ):
    b5 = colored(stat5,'yellow')
   elif (stat5 < 500):
    b5 = colored(stat5,'magenta')
   else:
    b5 = colored(stat5,'red')   
   print(f"[{met5}]To[ {url_c} ] > [",b5,"]")
   if (stat5 < 400 or stat5 > 499):
    af = open('./log/METHOD_RESULTS.txt','a')
    ah = af.write(f"[{met5}]To[ {url_c} ] > [{b5}]\n")
    af.close()
   else:
    pass
    
   # head   
   req6 = requests.head(url,headers=headers)
   stat6 = req6.status_code
   response6 = colored(req6.headers,'blue')
   if (stat6 < 300 ):
    b6 = colored(stat6,'blue')
   elif (stat6 < 400 ):
    b6 = colored(stat6,'yellow')
   elif (stat6 < 500):
    b6 = colored(stat6,'magenta')
   else:
    b6 = colored(stat6,'red')  
   # file writing condition state
   if (stat6 < 400 or stat6 > 499):
    af = open('./log/METHOD_RESULTS.txt','a')
    ah = af.write(f"[{met6}]To[ {url_c} ] > [{b6}]\n")
    af.close()
   else:
    pass
    
   print(f"[{met6}]To[ {url_c} ] > [",b6,"] Headers[",response6,"]")
   print(colored("---------------------------------------------------","red"))
