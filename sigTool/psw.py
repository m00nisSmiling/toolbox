from termcolor import colored
import requests
import random

def psw():
 #requests.get(f'https://eovzlu8cd49gpu1.m.pipedream.net/?tool=passwordGenerator:{list55}')
 print(colored('''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

             ====== ===== ==           ==
             =   == =      ==    =    ==
STRONG --    ====== =====   ==  ===  ==       --   GENERATOR
             =         ==    ==== ====
             =      =====     ==   ==    

First input is for "how many password do you need?" !!
L = Input Total Letters
N = Input Total Numbers
S = Input Total Symbols

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

''','red'))
 strings = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 numbers = ['1','2','3','4','5','6','7','8','9','0']
 symbols = ['$','%','^','*','(',')','_','+','|','}','{',':','?','>','<',';','.','!','#','-','&','@']
 #binarys = []

 password_count = int(input("Password count : "))

 for i in range(0,password_count):
  input_user1 = int(input("L: "))
  input_user2 = int(input("N: "))
  input_user3 = int(input("S: "))
 
  string_lst = []
  number_lst = []
  symbol_lst = []


  for i in range(0,input_user1):
   letter = strings[random.randint(0, len(strings) - 1)]
   string_lst.append(letter)

  for i in range(0,input_user2):
   number = numbers[random.randint(0, len(numbers) - 1)]
   number_lst.append(number)

  for i in range(0,input_user3):
   special = symbols[random.randint(0, len(symbols) - 1)]
   symbol_lst.append(special)

  password = string_lst + number_lst + symbol_lst
  random.shuffle(password)
  final = "".join(password)
  print(colored('PASSWORD >>> ','blue'),final)
 log_file = open('log/log.txt','a')
 log_file.write(f'[sub] strong password generator --> password count {password_count}\n')
 log_file.close()
psw()
