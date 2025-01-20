n = int(input())
def func(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return func(n-1) + func(n-2)
print(func(n))