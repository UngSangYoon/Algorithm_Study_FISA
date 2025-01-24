n = int(input())

def fac(x):
    if x < 2:
        return 1
    else: return x * fac(x-1)

num = list(str(fac(n)))[::-1] 
cnt = 0
for item in num:
    if item == '0':
        cnt += 1
    else: 
        print(cnt)
        break
