n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    print(fib[n])