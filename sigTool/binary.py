import requests
from termcolor import colored

log_file = open('log/log.txt','a')

def binary():
 #requests.get(f'https://eovzlu8cd49gpu1.m.pipedream.net/?tool=binaryEncoder:{list55}')
 text = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','(',',','$','-','@','#','+','=','/','\\','[',']',';','?','{','}','<','>','*','%','&','\'','"','|',':','!','^','_','.','1','2','3','4','5','6','7','8','9','0']
 binary = ['01100001','01100010','01100011','01100100','01100101','01100110','01100111','01101000','01101001','01101010','01101011','01101100','01101101','01101110','01101111','01110000','01110001','01110010','01110011','01110100','01110101','01110110','01110111','01111000','01111001','01111010','01000001','01000010','01000011','01000100','01000101','01000110','01000111','01001000','01001001','01001010','01001011','01001100','01001101','01001110','01001111','01010000','01010001','01010010','01010011','01010100','01010101','01010110','01010111','01011000','01011001','01011010','00101000','00101100','00100100','00101101','01000000','00100011','00101011','00111101','00101111','01011100','01011011','01011101','00111011','00111111','01111011','01111101','00111100','00111110','00101010','00100101','00100110','00100111','00100010','01111100','00111010','00100001','01011110','01011111','00101110','00110001','00110010','00110011','00110100','00110101','00110110','00110111','00111000','00111001','00110000']
 print(colored('''
++++++++++++++++++++++++++++++++++++++++++++++++++
         |ENCODER|
ooo      
o  o
ooo
o  o - i - n - a - r - y  
ooo  

[!] write count of your words
[!] write plain text to encode as binary string
+++++++++++++++++++++++++++++++++++++++++++++++++++
''','blue'))
 inp_len = input("Plain Text :")
 print('Length of string:',len(inp_len))
 input_text = inp_len

 listc = []
 for i in range(len(inp_len)):
  if input_text[i]==text[0]:
   listc.append(binary[0])
  elif input_text[i]==' ':
   listc.append('00100000')
  elif input_text[i]==text[1]:
   listc.append(binary[1])
  elif input_text[i]==text[2]:
   listc.append(binary[2])
  elif input_text[i]==text[3]:
   listc.append(binary[3])
  elif input_text[i]==text[4]:
   listc.append(binary[4])
  elif input_text[i]==text[5]:
   listc.append(binary[5])
  elif input_text[i]==text[6]:
   listc.append(binary[6])
  elif input_text[i]==text[7]:
   listc.append(binary[7])
  elif input_text[i]==text[8]:
   listc.append(binary[8])
  elif input_text[i]==text[9]:
   listc.append(binary[9])
  elif input_text[i]==text[10]:
   listc.append(binary[10])
  elif input_text[i]==text[11]:
   listc.append(binary[11])
  elif input_text[i]==text[12]:
   listc.append(binary[12])
  elif input_text[i]==text[13]:
   listc.append(binary[13])
  elif input_text[i]==text[14]:
   listc.append(binary[14])
  elif input_text[i]==text[15]:
   listc.append(binary[15])
  elif input_text[i]==text[16]:
   listc.append(binary[16])
  elif input_text[i]==text[17]:
   listc.append(binary[17])
  elif input_text[i]==text[18]:
   listc.append(binary[18])
  elif input_text[i]==text[19]:
   listc.append(binary[19])
  elif input_text[i]==text[20]:
   listc.append(binary[20])
  elif input_text[i]==text[21]:
   listc.append(binary[21])
  elif input_text[i]==text[22]:
   listc.append(binary[22])
  elif input_text[i]==text[23]:
   listc.append(binary[23])
  elif input_text[i]==text[24]:
   listc.append(binary[24])
  elif input_text[i]==text[25]:
   listc.append(binary[25])
  elif input_text[i]==text[26]:
   listc.append(binary[26])
  elif input_text[i]==text[27]:
   listc.append(binary[27])
  elif input_text[i]==text[28]:
   listc.append(binary[28])
  elif input_text[i]==text[29]:
   listc.append(binary[29])
  elif input_text[i]==text[30]:
   listc.append(binary[30])
  elif input_text[i]==text[31]:
   listc.append(binary[31])
  elif input_text[i]==text[32]:
   listc.append(binary[32])
  elif input_text[i]==text[33]:
   listc.append(binary[33])
  elif input_text[i]==text[34]:
   listc.append(binary[34])
  elif input_text[i]==text[35]:
   listc.append(binary[35])
  elif input_text[i]==text[36]:
   listc.append(binary[36])
  elif input_text[i]==text[37]:
   listc.append(binary[37])
  elif input_text[i]==text[38]:
   listc.append(binary[38])
  elif input_text[i]==text[39]:
   listc.append(binary[39])
  elif input_text[i]==text[40]:
   listc.append(binary[40])
  elif input_text[i]==text[41]:
   listc.append(binary[41])
  elif input_text[i]==text[42]:
   listc.append(binary[42])
  elif input_text[i]==text[43]:
   listc.append(binary[43])
  elif input_text[i]==text[44]:
   listc.append(binary[44])
  elif input_text[i]==text[45]:
   listc.append(binary[45])
  elif input_text[i]==text[46]:
   listc.append(binary[46])
  elif input_text[i]==text[47]:
   listc.append(binary[47])
  elif input_text[i]==text[48]:
   listc.append(binary[48])
  elif input_text[i]==text[49]:
   listc.append(binary[49])
  elif input_text[i]==text[50]:
   listc.append(binary[50])
  elif input_text[i]==text[51]:
   listc.append(binary[51])
   #special character
  elif input_text[i]==text[52]:
   listc.append(binary[52])
  elif input_text[i]==text[53]:
   listc.append(binary[53])
  elif input_text[i]==text[54]:
   listc.append(binary[54])
  elif input_text[i]==text[55]:
   listc.append(binary[55])
  elif input_text[i]==text[56]:
   listc.append(binary[56])
  elif input_text[i]==text[57]:
   listc.append(binary[57])
  elif input_text[i]==text[58]:
   listc.append(binary[58])
  elif input_text[i]==text[59]:
   listc.append(binary[59])
  elif input_text[i]==text[60]:
   listc.append(binary[60])
  elif input_text[i]==text[61]:
   listc.append(binary[61])
  elif input_text[i]==text[62]:
   listc.append(binary[62])
  elif input_text[i]==text[63]:
   listc.append(binary[63])
  elif input_text[i]==text[64]:
   listc.append(binary[64])
  elif input_text[i]==text[65]:
   listc.append(binary[65])
  elif input_text[i]==text[66]:
   listc.append(binary[66])
  elif input_text[i]==text[67]:
   listc.append(binary[67])
  elif input_text[i]==text[68]:
   listc.append(binary[68])
  elif input_text[i]==text[69]:
   listc.append(binary[69])
  elif input_text[i]==text[70]:
   listc.append(binary[70])
  elif input_text[i]==text[71]:
   listc.append(binary[71])
  elif input_text[i]==text[72]:
   listc.append(binary[72])
  elif input_text[i]==text[73]:
   listc.append(binary[73])
  elif input_text[i]==text[74]:
   listc.append(binary[74])
  elif input_text[i]==text[75]:
   listc.append(binary[75])
  elif input_text[i]==text[76]:
   listc.append(binary[76])
  elif input_text[i]==text[77]:
   listc.append(binary[77])
  elif input_text[i]==text[78]:
   listc.append(binary[78])
  elif input_text[i]==text[79]:
   listc.append(binary[79])
  elif input_text[i]==text[80]:
   listc.append(binary[80])
  elif input_text[i]==text[81]:
   listc.append(binary[81])
  elif input_text[i]==text[82]:
   listc.append(binary[82])
  elif input_text[i]==text[83]:
   listc.append(binary[83])
  elif input_text[i]==text[84]:
   listc.append(binary[84])
  elif input_text[i]==text[85]:
   listc.append(binary[85])
  elif input_text[i]==text[86]:
   listc.append(binary[86])
  elif input_text[i]==text[87]:
   listc.append(binary[87])
  elif input_text[i]==text[88]:
   listc.append(binary[88])
  elif input_text[i]==text[89]:
   listc.append(binary[89])
  elif input_text[i]==text[90]:
   listc.append(binary[90])
   
  else:
   listc.append(' ')

 strings = ''.join(listc)

 print(colored('''
 -------------------------------------------ENCODED STRINGS------------------------------------------------------''','red'))
 print(strings)
 print(colored('''
 -------------------------------------------ENCODED STRINGS------------------------------------------------------''','red'))
 log_file = open('log/log.txt','a')
 log_file.write(f'[sub] Binary Encoder --> string {input_text}\n')
 log_file.close()

binary()
