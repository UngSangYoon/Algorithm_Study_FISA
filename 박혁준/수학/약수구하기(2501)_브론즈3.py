num, n = map(int, input().split())

cnt = 0
ans = 0

for i in range(1,num+1):
    if (num%i)==0:
        cnt+=1
    if cnt==n:
        ans = i
        break

print(ans)