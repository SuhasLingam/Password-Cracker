import hashlib


flag = 0
pass_hash = input("Enter a MD5 Hash To Crack : \n")

wordlist = input("File Name : \n")

try:
    pass_file = open(wordlist , "r")

except:
    print("File Not Found!!!")
    quit()    

    
    
for word in pass_file:
    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()
    
 
 
    
    
if digest == pass_hash:
    print("Password Found")
    print("Password is : " + word)
    flag = 1
    
if flag == 0:
    print("Password Not Found")    
            
