#
n = int(input())
x = [-1] * (n+3)
x[0] = 0; x[1] = 1; x[2] = 1

def fibo(k):
    if x[k] != -1:
        return x[k]
    x[k] = fibo(k-1) + fibo(k-2)
    return x[k] 

print(fibo(n))