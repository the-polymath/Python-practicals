# 9.1 Write a python program to implement ceaser cipher

def ceasar(string, key):
    temp = ""
    for i in string:
        if i == " ":
            temp += i
            continue
        ch = ord(i)
        if ch > 64 and ch < 91:
            temp += chr((ch - 65 + key) % 26 + 65)
        elif ch > 96 and ch < 123:
            temp += chr((ch - 97 + key) % 26 + 97)

    return temp


plaintext = input("Enter the plaintext : ")
key = int(input("Enter the Key for Ceasar Cipher : "))
ciphertext = ceasar(plaintext, key)
print("The encrypted text is : ", ciphertext)
