# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

s = []

n = int(input())
num = list(map(int, input().split()))
for j in range(len(num)):
    list_ = []
    for i in range(1, max(num)+1):
        if num[j]%i == 0:
            list_.append(i)
    if len(list_) == 2:
        s.append(num[j])

print(len(s))