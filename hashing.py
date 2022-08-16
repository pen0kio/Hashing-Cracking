#!/usr/bin/python3
from colorama import Fore
import hashlib

# Function Decrpt MD5 Hash
def md5b():
    passwordHash = input('Enter MD5 Hash Value: ')
    wordList= input("Enter the passwordlist(Path+Filename): ")
    # Code to clear screen
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    passwords = open(wordList, 'r')
    for word in passwords:
        print(Fore.YELLOW + '[*] Trying: ' + word.strip('\n'))
        encodeWord = word.encode('UTF-8')
        md5Hash = hashlib.md5(encodeWord.strip()).hexdigest()    
        if md5Hash == passwordHash:
            print(Fore.GREEN + '[+] Password Found: ' + word)
            exit(0)
        else:
            pass
    passwords.close()
    print('[-] Password Not in List')

# Function Decrpt SHA1 Hash
def sha1d():
    passwordHash = input('Enter SHA1 Hash Value: ')
    wordList= input("Enter the passwordlist(Path+Filename): ")
    # Code to clear screen
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    passwords = open(wordList, 'r')
    for word in passwords:
        print(Fore.YELLOW + '[*] Trying: ' + word.strip('\n'))
        encodeWord = word.encode('UTF-8')
        md5Hash = hashlib.sha1(encodeWord.strip()).hexdigest()    
        if md5Hash == passwordHash:
            print(Fore.GREEN + '[+] Password Found: ' + word)
            exit(0)
        else:
            pass
    passwords.close()
    print('[-] Password Not in List')

# Function Decrpt SHA224 Hash
def sha224d():
    passwordHash = input('Enter SHA224 Hash Value: ')
    wordList= input("Enter the passwordlist(Path+Filename): ")
    # Code to clear screen
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    passwords = open(wordList, 'r')
    for word in passwords:
        print(Fore.YELLOW + '[*] Trying: ' + word.strip('\n'))
        encodeWord = word.encode('UTF-8')
        md5Hash = hashlib.sha224(encodeWord.strip()).hexdigest()    
        if md5Hash == passwordHash:
            print(Fore.GREEN + '[+] Password Found: ' + word)
            exit(0)
        else:
            pass
    passwords.close()
    print('[-] Password Not in List')

# Function Decrpt SHA256 Hash
def sha256d():
    passwordHash = input('Enter SHA256 Hash Value: ')
    wordList= input("Enter the passwordlist(Path+Filename): ")
    # Code to clear screen
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    passwords = open(wordList, 'r')
    for word in passwords:
        print(Fore.YELLOW + '[*] Trying: ' + word.strip('\n'))
        encodeWord = word.encode('UTF-8')
        md5Hash = hashlib.sha256(encodeWord.strip()).hexdigest()    
        if md5Hash == passwordHash:
            print(Fore.GREEN + '[+] Password Found: ' + word)
            exit(0)
        else:
            pass
    passwords.close()
    print('[-] Password Not in List')

# Function Decrpt SHA512 Hash
def sha512d():
    passwordHash = input('Enter SHA512 Hash Value: ')
    wordList= input("Enter the passwordlist(Path+Filename): ")
    # Code to clear screen
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    passwords = open(wordList, 'r')
    for word in passwords:
        print(Fore.YELLOW + '[*] Trying: ' + word.strip('\n'))
        encodeWord = word.encode('UTF-8')
        md5Hash = hashlib.sha512(encodeWord.strip()).hexdigest()    
        if md5Hash == passwordHash:
            print(Fore.GREEN + '[+] Password Found: ' + word)
            exit(0)
        else:
            pass
    passwords.close()
    print('[-] Password Not in List')

# Function Creates Hashes
def createhashes():
    hashValue = input('Enter String to Hash: ')
    hashmd5 = hashlib.md5()
    hashmd5.update(hashValue.encode())
    print('MD5 Hash: ' + hashmd5.hexdigest())
    hashsha1 = hashlib.sha1()
    hashsha1.update(hashValue.encode())
    print('SHA1 Hash: ' + hashsha1.hexdigest())
    hashsha224 = hashlib.sha224()
    hashsha224.update(hashValue.encode())
    print('SHA224 Hash: ' + hashsha224.hexdigest())
    hashsha256 = hashlib.sha256()
    hashsha256.update(hashValue.encode())
    print('SHA256 Hash: ' + hashsha256.hexdigest())
    hashsha512 = hashlib.sha512()
    hashsha512.update(hashValue.encode())
    print('SHA512 Hash: ' + hashsha512.hexdigest())

print(Fore.YELLOW + r"""  ______            _              ___  ___ _       _                 
  | ___ \          | |             |  \/  |(_)     | |                
  | |_/ /_   _   __| | _ __  __ _  | .  . | _  ___ | |__   _ __  __ _ 
  |    /| | | | / _` || '__|/ _` | | |\/| || |/ __|| '_ \ | '__|/ _` |
  | |\ \| |_| || (_| || |  | (_| | | |  | || |\__ \| | | || |  | (_| |
  \_| \_|\__,_| \__,_||_|   \__,_| \_|  |_/|_||___/|_| |_||_|   \__,_|
                                                                   """)
print(Fore.RED + "  ****************************************************************")
print(Fore.YELLOW + "  * Copyright of Rudra Kumar Mishra,                             *")
print(Fore.BLUE + "  * Creates hashes md5, sha1, sha224, sha256, sha512.            *")
print(Fore.BLUE + "  * Checks more than a Million passwords per minute.             *")
print(Fore.RED + "  ****************************************************************\n")

# Printing Options
print(Fore.GREEN + "Enter 1 to Create Hash        *")
print(Fore.GREEN + "Enter 2 to Decrpt MD5 Hash    *")
print(Fore.GREEN + "Enter 3 to Decrpt SHA1 Hash   *")
print(Fore.GREEN + "Enter 4 to Decrpt SHA224 Hash *")
print(Fore.GREEN + "Enter 5 to Decrpt SHA256 Hash *")
print(Fore.GREEN + "Enter 6 to Decrpt SHA512 Hash *")

# Enter choice from user
choice = str(input(Fore.GREEN + "Enter (1-6) as choice: "))

if(choice=="1"):
    # Function to create Hashes
    createhashes()
elif(choice=="2"):
    # Function to decrpt MD5 Hash
    md5b()
elif(choice=="3"):
    # Function to decrpt SHA1 Hash
    sha1d()
elif(choice=="4"):
    # Function to decrpt SHA224 Hash
    sha224d()
elif(choice=="5"):
    # Function to decrpt SHA256 Hash
    sha256d()
elif(choice=="6"):
    # Function to decrpt SHA512 Hash
    sha512d()
else:
    print(Fore.RED + "Wrong Input   ****************************************************\n")