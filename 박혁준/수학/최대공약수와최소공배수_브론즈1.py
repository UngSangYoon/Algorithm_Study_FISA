a, b = map(int, input().split())

for i in reversed(range(1, a+1 if a<b else b+1)):
    if (a%i)==0 and (b%i)==0:
        print(i)
        print(int((a*b)/i))
        break
