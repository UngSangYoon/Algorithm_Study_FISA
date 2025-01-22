


def hanoi(n, a, b, c):
    if n == 1:
        print(f"{a} {c}")
    else:
        hanoi(n - 1, a, c, b)
        print(f"{a} {c}")
        hanoi(n - 1, b, a, c)


n = int(input())
cnt = 1
for _ in range(n):
    cnt *= 2
print(cnt - 1)
hanoi(n, 1, 2, 3)

