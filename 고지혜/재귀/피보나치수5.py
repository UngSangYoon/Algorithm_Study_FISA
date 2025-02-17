def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:  # 무한 재귀 방지
        return 1
    else:
        n = Fibonacci(n-1) + Fibonacci(n-2)
        return n
     
n = int(input())
print(Fibonacci(n))


