N = int(input())

rest = 1000-N
ans = 0

ans += rest // 500
rest = rest % 500

ans += rest // 100
rest = rest % 100

ans += rest // 50
rest = rest % 50

ans += rest // 10
rest = rest % 10

ans += rest // 5
rest = rest % 5

ans += rest

print(ans)