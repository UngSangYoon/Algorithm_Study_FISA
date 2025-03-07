'''
< 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램 > 

ex. t=4
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
-> 7
'''
# import sys

# def sum_onetwothree(t, case):
#     max_t = max(case)  # 입력값 중 가장 큰 t
#     dp = [0] * (max_t + 1)

#     dp[1] = 1  # 1-> 1
#     # dp[2] = 2  # 1+1/2-> 2
#     # dp[3] = 4  # 1+1+1/1+2/2+1/3-> 4
#     if max_t >= 2:
#         dp[2] = 2
#     if max_t >= 3:
#         dp[3] = 4

#     for i in range(4, t + 1):  # 4~t까지
#         # t=4-> 7
#         # 1+1+1+1/1+2+1/2+1+1/3+1  3
#         # 1+1+2/2+2  2
#         # 1+3  1
#         # t=5-> 13
#         # (1+1+1+1)+1/1+1+2+1/1+2+1+1/2+1+1+1/2+2+1/3+1+1/1+3+1  4
#         # (1+1+1)+2/1+2+2/2+1+2/3+2   3
#         # (1+1)+3/2+3  2
#         dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
#     return dp[i]

# t = int(sys.stdin.readline().strip())
# case = [int(sys.stdin.readline().strip()) for _ in range(t)]

# for n in case:
#     print(sum_onetwothree(n, case))
# => 런타임 에러, 함수에는 t가 아닌 값으로 넣어줘야함(case)

import sys 

def sum_onetwothree(n, case):
    max_t = max(case)  # 입력값 중 가장 큰 t
    dp = [0] * (max_t + 1)
    dp[1] = 1  # 1-> 1
    dp[2] = 2
    # 1+1+1/2+1  2
    # 1+2  1
    # 3  3
    '''
    dp[3]=4 직접 설정해버리면, 
    n=1일 때 dp는 [0,0]인데 배열 범위 초과 오류가 발생해서 if문으로 조건 설정
    그래서 dp[2]는 배열크기가 이미 할당되어 있어서 초과 오류는 발생하지 않음
    '''
    if max_t >= 3:  
        dp[3] = 4

    for i in range(4, max_t + 1):  # 4~t까지
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp[n]

# t = int(input())
# case = [int(input()) for _ in range(t)]
t = int(sys.stdin.readline().strip())
case = [int(sys.stdin.readline().strip()) for _ in range(t)]

for n in case:
    print(sum_onetwothree(n, case))