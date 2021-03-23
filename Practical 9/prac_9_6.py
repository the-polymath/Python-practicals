# Write a python program to implement RSA Algorithm
import libnum
def rsa(p, q, m):
    n = p * q
    totient = (p-1)*(q-1)
    print(" n = ", n)
    print("phi(n) = ", totient)
    print()
    e = int(input("Enter a prime number for Key 'e' (should be less than phi(n) ) : "))
    c = encrypt(m, e, n)

def encrypt(m, e, n):
    ciphertext = (m ** e) % n
    print("Ciphertext of RSA algo is : ", ciphertext)
    return ciphertext

p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))
message = int(input("Enter a message: "))
rsa(p, q, message)
