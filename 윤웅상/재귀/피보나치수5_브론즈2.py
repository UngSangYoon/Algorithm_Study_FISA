n = int(input())

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
 
    return fibo(n-1) + fibo(n-2)

print(fibo(n))
#fibo(2) = fibo(1) + fibo(0) = 1
#fibo(3) = fibo(2) + fibo(1) = 2