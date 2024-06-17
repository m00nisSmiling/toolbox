import requests
import random
import json
from termcolor import colored


print(colored('''
             |---||||||=----
           ____________________
          [____________________]
          [_EXPLOIT_-_DATABASE_]
          [____________________]
          [___BY________m00n___]
          [____________________]

''','blue'))
inp1 = input(colored("Search Term : ",'red'))
log_file = open('log/log.txt','a')
log_file.write(f'[sub] exploit database dump --> search term : {inp1}\n')
log_file.close()

iam = random.randint(0,999)

Headers = {"cookie": "XSRF-TOKEN=eyJpdiI6ImpodFdkMkcreWFKdjlmTzdJNVJpSHc9PSIsInZhbHVlIjoiNmJRd2tyOXRGb3BaSkhKZnpCOXZWTEZkYjRkXC8zSTV5b0IwdW5oeVlqQmtnRkdmUVlnZUpqUklSbmVEcDNPMEIiLCJtYWMiOiJmODVjZjg4YTdiNGJhN2E4ZGRiMzIwMWM4ZTYyYjI4ZjFiODk3MDU1YTMzMGNhMWQ4MTRlNGQ1ZGY5Y2EzMjBhIn0%3D; exploit_database_session=eyJpdiI6IlZCcWVTa25lK2tTRFE1dTBUYVdkY2c9PSIsInZhbHVlIjoiUGdtbnNnUXpDTHZ2NFpaOStaNkh5U1wvYk1DVkM1S2NvejM4M0tkZk04UUJ4djErWjRkdDl3VUZnYmRYUERMTnkiLCJtYWMiOiIzZWQyNDk3MjNlNmJhZGRmMmYwNzdiOGEyYzcyNjAzZDRjY2RmOWViNWIwYmFlMzRhYjJhMTU1OTk3NDI2N2UxIn0%3D; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1718602076292%2Cregion:%27MM%27}; _ga=GA1.3.1758465357.1718602077; _gid=GA1.3.1700953141.1718602077; _ga_N0K6XSDCRJ=GS1.3.1718602077.1.1.1718602235.60.0.0","User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
"Accept": "application/json, text/javascript, */*; q=0.01",
"X-Requested-With": "XMLHttpRequest",
"Sec-Fetch-Site": "same-origin"}

url = f"https://www.exploit-db.com/?draw=6&columns%5B0%5D%5Bdata%5D=date_published&columns%5B0%5D%5Bname%5D=date_published&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=download&columns%5B1%5D%5Bname%5D=download&columns%5B1%5D%5Bsearchable%5D=false&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=application_md5&columns%5B2%5D%5Bname%5D=application_md5&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=verified&columns%5B3%5D%5Bname%5D=verified&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=description&columns%5B4%5D%5Bname%5D=description&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=type_id&columns%5B5%5D%5Bname%5D=type_id&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=platform_id&columns%5B6%5D%5Bname%5D=platform_id&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=author_id&columns%5B7%5D%5Bname%5D=author_id&columns%5B7%5D%5Bsearchable%5D=false&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=code&columns%5B8%5D%5Bname%5D=code.code&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=id&columns%5B9%5D%5Bname%5D=id&columns%5B9%5D%5Bsearchable%5D=false&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=9&order%5B0%5D%5Bdir%5D=desc&start=0&length=15&search%5Bvalue%5D={inp1}&search%5Bregex%5D=false&author=&port=&type=&tag=&platform=&_=1718602234{iam}"

ab = requests.get(f"{url}",headers=Headers).text
jsp = json.loads(ab)

ac = jsp['recordsTotal']
ae = jsp['recordsFiltered']
ad = jsp['data']


print(f"\n          Total Records [ {ac} ]\n            EXPLOIT FOUND [ {ae} ]\n")
print(colored("-------------------------------------------",'red'))
for i in range(0,5):
 try:
  aba = ad[i]['description'][0]
  abb = ad[i]['description'][1]
  abd = ad[i]['platform']['platform']
  abe = ad[i]['date_published']
  abf = ad[i]['type_id']
  abc = ad[i]['description'][0]
 except IndexError:
  pass
 else:

  print(colored("|  CVE-ID: ",'red'),aba)
  print(colored("|  Description: ",'red'),abb)
  print(colored("|  Platform: ",'red'),abd)
  print(colored("|  Published Date: ",'red'),abe)
  print(colored("|  Vulnerable Type: ",'red'),abf)
  exp = f"https://www.exploit-db.com/download/{abc}"
  print(colored("|  Exploit-Download: ",'red'),exp)
  print(colored("-------------------------------------------",'red'))
