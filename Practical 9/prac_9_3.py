# 9.3 Write a python program to implement reverse ceaser cipher

def reverseceasar(string, key):
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

    temp = temp[::-1]
    return temp

plaintext = input("Enter the plaintext : ")
key = int(input("Enter the Key for Ceasar Cipher : "))
ciphertext = reverseceasar(plaintext, key)
print("The encrypted text is : ", ciphertext)
