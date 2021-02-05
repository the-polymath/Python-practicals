def pattern(N):
    # forward triangle
    for i in range(0,N):
        for j in range(0, i+1):
            print("* ",end="")
        print()
    # backward triangle
    for i in range(1, N):
        for j in range(N, i, -1):
            print("* ", end="")
        print()

N = int(input())
print()
pattern(N)
