num = list(map(int,input("").split()))
b = set(num)

if len(b) == 3:
    print(max(num) * 100)
elif len(b) == 2:
    c = sum(num) - sum(b)
    print(1000 + c * 100)
else:
    print(10000 + num.pop() * 1000)
