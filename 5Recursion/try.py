def adder(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return adder(n - 1) + adder(n-2)

ans = adder(6)
print(ans)