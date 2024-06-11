import requests
from termcolor import colored
import urllib.parse
import dns
import dns.resolver

def dnsrec():
 #requests.get(f'https://eovzlu8cd49gpu1.m.pipedream.net/?tool=dnsRecordFinder:{list55}')
 print(colored(''' 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

000000  1111111
00  00  11      
000000  11111   00000
00   00 11  DNS 00
00    001111111 00000

[!] Input Only dns without http or https
[!] Don't input subdomain
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

''','blue'))
 name = input(colored("Enter Domain : ",'red'))

 print('''
---------
[1] A 
[2] AAAA
[3] MX
[4] NS
[5] TXT
[6] SOA
[7] ALL
---------
''')
 option = input(colored("Option ? : ",'red'))

 if option == "1":
  a=dns.resolver.query(name,'A')
  print(a.rrset)
 elif option == "2":
  aaaa=dns.resolver.query(name,'AAAA')
  print(aaaa.rrset)
 elif option == "3":
  mx=dns.resolver.query(name,'MX')
  print(mx.rrset)
 elif option == "4":
  ns=dns.resolver.query(name,'NS')
  print(ns.rrset)
 elif option == "5":
  txt=dns.resolver.query(name,'TXT')
  print(txt.rrset)
 elif option == "6":
  soa=dns.resolver.query(name,'SOA')
  print(soa.rrset)
 elif option == "7":
  for qtype in 'A','AAAA','MX','NS','TXT','SOA':
   answer= dns.resolver.query(name,qtype,raise_on_no_answer=False)
   if answer.rrset is not None:
    print(answer.rrset)
 log_file = open('log/log.txt','a')
 log_file.write(f'[sub] DNS Record Finder --> dns {name} --> record {option}\n')
 log_file.close()
 
dnsrec()
