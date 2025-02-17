def fac(n):
    if n <= 1:
        ans = 1
    else:
        ans = fac(n-1) * n
        
    return ans

print(fac(int(input())))