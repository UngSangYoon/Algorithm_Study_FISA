'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''

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



