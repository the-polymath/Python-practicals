def fibo(n):
    a = 0
    b = 1
    print(a, b, end=" ")
    for _ in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

N = int(input())
print("\nThe series is : ")
fibo(N)
