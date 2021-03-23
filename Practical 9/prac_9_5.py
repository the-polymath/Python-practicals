# Write a python program to implement Block cipher(SHA1, MD5)
import hashlib

def MD5(plaintext):
    return hashlib.md5(plaintext.encode())

def SHA(plaintext):
    return hashlib.sha1(plaintext.encode())



plaintext = input('Enter the text : ')
cipher = input("Which block cipher (SHA1, MD5) : ")

if cipher == "SHA1":
    ciphertext = SHA(plaintext)
else:
    ciphertext = MD5(plaintext)

print("The encrypted text is : ", ciphertext.hexdigest())
