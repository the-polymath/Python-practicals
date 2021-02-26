def reverse(var):
    r = 0
    while var > 0:
        d = var % 10
        r = (r * 10) + d
        var = var // 10

    return r

N = int(input())
rev = reverse(N)
print(rev)
