N = int(input())
ans = []

for i in range(N):
    now = input("")
    nowsum = 0
    plus = 1
    for i in now:
        if i == 'O':
            nowsum += plus
            plus += 1
        else:
            plus = 1
            
        

    ans.append(nowsum)
for i in ans:
    print(i)