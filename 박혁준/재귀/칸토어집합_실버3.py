def s(n):
    if (n<=1):
        return ('-')
    else:
        return f"{s(n//3)}{' '*(n//3)}{s(n//3)}"

while True:
    try:
        n = int(input())
        n = 3**n
        print(s(n))       
    except:
        break