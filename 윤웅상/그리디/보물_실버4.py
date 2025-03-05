N = int(input())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

s1 = sorted(s1)
s2 = sorted(s2)[::-1]

ans = 0
for x, y in zip(s1, s2):
    ans += x * y

print(ans)