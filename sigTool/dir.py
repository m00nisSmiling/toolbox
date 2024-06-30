from termcolor import colored
import requests


def dir():
 #requests.get(f'https://eovzlu8cd49gpu1.m.pipedream.net/?tool=directoryEnumerator:{list55}')
 print(colored('''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

//////  ///////// ///////
//   //    //     //    //
//    //   //     ///////
//   //    //     //   //
////// /////////  //    ////moonissmiling

[!] input a url end with "/" 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

''','blue'))
 dns = input(colored("$dns$ ",'red'))
 log_file = open('log/log.txt','a')
 log_file.write(f'[sub] directory bruteforce --> domain {dns}\n')
 log_file.close()
 
 txtlst = open("./wordlists/dir_list.txt").read()
 directories = txtlst.splitlines()

 for dir in directories:
  directory = f"{dns}{dir}"
  print(colored(f"[Getting....] {directory}","red")) 
  fail=requests.get(directory)
  if fail.status_code==404:
   pass
  else:
   print(colored("[directory] ",'blue'),directory)

dir()
