def check(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char in vowels:
        print("It is Vowel")
    else:
        print("It is consonant")

char = input()
check(char)
