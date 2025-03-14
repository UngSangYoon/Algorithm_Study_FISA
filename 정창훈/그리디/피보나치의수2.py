n = int(input())
fibonach = [0, 1]
for i in range(2, n+1):
    fibonach.append(fibonach[i-1] + fibonach[i-2])

print(fibonach[n])