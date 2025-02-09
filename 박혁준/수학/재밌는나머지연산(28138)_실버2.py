n,m = map(int, input().split())
ans = 0
tmp = 0
for i in range(1,n):
    if (n%i)==m:
        tmp = i
        break

for j in range(tmp,n+1,tmp):
            if (n%j)==0:
                ans+=j


print(ans)



# n,m = map(int, input().split())
# ans = 0
# for i in range(1,n):
#     if (n%i)==m:
#         ans += i

# print(ans)