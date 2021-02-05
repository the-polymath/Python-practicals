def printprime(n):
    num = n - 1
    n = 3
    print("2 ", end="")
    # counts till first n
    while num > 0:

        # checks each prime number
        for i in range(2, (n//2)+1):
            if n % i == 0:
                n += 1
                break
        else:
            print(n, end=" ")
            num -= 1
            n += 1

N = int(input())
printprime(N)
