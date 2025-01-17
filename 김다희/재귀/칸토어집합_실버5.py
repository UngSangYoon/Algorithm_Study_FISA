# 문제
# 칸토어 집합은 0과 1사이의 실수로 이루어진 집합으로, 구간 [0, 1]에서 시작해서 각 구간을 3등분하여 가운데 구간을 반복적으로 제외하는 방식으로 만든다.
# 전체 집합이 유한이라고 가정하고, 다음과 같은 과정을 통해서 칸토어 집합의 근사를 만들어보자.

from sys import stdin

input = stdin.readline

def cantor(n): # 칸토어 집합 생성, n: 칸토어 집합 길이
    if n == 1: # base case
        return ["-"]

    previous = cantor(n // 3) # reculsive case? 현재 길이 3등분
    space = [" "] * (n // 3) # 가운데 공백
    print('길이:',n, "".join(previous + space + previous))
    return previous + space + previous 

while True:
    try:
        N = int(input())
        print("".join(cantor(3 ** N)))
    except:
        break