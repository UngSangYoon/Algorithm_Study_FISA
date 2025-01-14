# 27433 번

'''
문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 20)이 주어진다.

출력
첫째 줄에 N!을 출력한다.
'''

# 풀이 1 번

num = int(input())

def solution(n):
    # 코드 멈추는 부분
    if n == 0:
        return 1
    # 자기 호출 부분
    else:
        return solution(n-1) * n
    
print(solution(num))