T = int(input())

def fin(n):
    if n == 0:
        return 1
    else:
        sum = T * n
        return f"{T} * {n} = {sum}"
    
for i in range(1,10):
    print(fin(i))