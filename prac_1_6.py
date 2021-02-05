def armstrong(N):
    length = len(N)
    arm = 0
    for i in N:
        arm = arm + (int(i) ** length)

    if arm == int(N):
        print("It is Armstrong!!")
    else:
        print('It is not Armstrong!!')

N = input()
armstrong(N)
