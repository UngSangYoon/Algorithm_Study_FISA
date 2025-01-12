import math

def func1(num): 
    if num < 2:  # 1은 소수 아님, 
        return False
    for i in range(2, int(math.sqrt(num)) + 1):  # 2부터 sqrt(num)까지 나누기
        if num % i == 0: 
            return False
    return True

# 입력 받기
count = int(input())  # 수의 개수
num = list(map(int, input().split()))  # N개의 수

fun_count = sum(1 for i in num if func1(i))  # True 항목 개수 계산
print(fun_count)



