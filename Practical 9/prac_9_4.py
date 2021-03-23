# Write a python program to implement Transposition cipher

def encode(plaintext, key):
    key_length = len(key)
    ciphertext = ""
    for i in range(0, key_length):
        for t in range(i, len(plaintext), key_length):
            ciphertext += plaintext[t]

    return ciphertext

plaintext = input("Enter the Text : ")
key = input("Enter the Key : ")

ciphertext = encode(plaintext, key)
print("The encrypted string is : ", ciphertext)
