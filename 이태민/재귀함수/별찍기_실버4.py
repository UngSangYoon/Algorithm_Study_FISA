# 별 찍기 - 10994번 
# 어려워서 답지 봄.

num = int(input())
li = [[" " for _ in range(4 * num - 3)] for _ in range(4 * num - 3)]

# 재귀함수로 풀기
def star(n, x, y):
    if n == 1:
        li[x][y] = "*"
        return
    l = 4 * n - 3
    for i in range(l):
        li[x][y + i] = "*"
        li[x + i][y] = "*"
        li[x + l - 1][y + i] = "*"
        li[x + i][y + l - 1] = "*"
    star(n - 1, x + 2, y + 2)

star(num, 0, 0)

for _ in li:
    print("".join(_))