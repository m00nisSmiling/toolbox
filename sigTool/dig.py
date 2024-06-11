import os 
from termcolor import colored

filei = input(colored("filename:","blue"))
file = open(filei).read()
file1 = file.splitlines()

print(colored("Dig Results -----------------------------------------","red"))
for o in file1:
 log_file = open('log/log.txt','a')
 log_file.write(f'[sub] dns digger is starting----> filename:{filei} ---> dns:{o}\n')
 log_file.close()
 os.system(f"dig {o}")
