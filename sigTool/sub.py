import requests
from termcolor import colored

def sub():
 #requests.get(f'https://eovzlu8cd49gpu1.m.pipedream.net/?tool=subfinder:{list55}')
 print(colored('''
++++++++++++++++++++++++++++++++++++++++++++++

///////  //   // ///////
//       //   // //    //
//////// //   // ///////
      // //   // //    //
 /////// /////// //////  moonissmiling

[!] input only host name like "example.com"
++++++++++++++++++++++++++++++++++++++++++++++

''','red'))
 inpute = input(colored("[hostname] ]>",'blue'))
 log_file = open('log/log.txt','a')
 log_file.write(f'[sub] subdomain finder --> hostname {inpute}\n')
 log_file.close()
 
 sublist = open("./wordlists/subdomains.txt").read()
 subdomains = sublist.splitlines()

 for sub in subdomains:
   subdom=f"https://{sub}.{inpute}"
   try:
     requests.get(subdom)
   except requests.ConnectionError:
    pass
   else:
    print(colored(subdom,'red'))
  
sub()
  
