'''
<수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합 구하는 프로그램>
- 첫째 줄에 수의 개수 N, 합을 구해야 하는 횟수 M
- 둘째 줄에는 N개의 수
- 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j
=> 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력

data = [5, 4, 3, 2, 1]
dp   = [0, 0, 0, 0, 0, 0]
dp[0] = data[0] = 5
-> dp[1] = data[0] = 5
dp[1] = data의 index 0부터 1까지의 합 = (data[0]) + data[1] = dp[0] + data[1] = 5 + 4 = 9
-> dp[2] = dp[1] + data[1] 
dp[2] = data의 index 0부터 2까지의 합 = (data[0] + data[1]) + data[2] = dp[1] + data[2] = 9 + 3 = 12
-> dp[3] = dp[2] + data[2]
dp[3] = data의 index 0부터 3까지의 합 = (data[0] + data[1] + data[2]) + data[3] = dp[2] + data[3] = 12 + 2 = 14
-> dp[4] = dp[3] + data[3]
dp[4] = data의 index 0부터 4까지의 합 = (data[0] + data[1] + data[2] + data[3]) + data[4] = dp[3] + data[4] = 14 + 1 = 15
-> dp[5] = dp[4] + data[4]
=> dp = [5, 9, 12, 14, 15] -> dp = [0, 5, 9, 12, 14, 15]
구간 i~j에서
i가 1, j가 3이라면 -> dp[3] - dp[1-0] = 12 - 0 = 12
i가 2, j가 4라면 -> dp[4] - dp[2-1] = 14 - 5 = 9
i가 5, j가 5라면 -> dp[5] - dp[5-1] = 15 - 14 = 1
'''
# import sys

# n, m = map(int, sys.stdin.readline().split())  # 5 3 
# data = list(map(int, sys.stdin.readline().split()))  # n개의 수만큼 입력, 5 4 3 2 1

# def prefix_sum(data, n, m):
#     dp = [0] * n  # dp = [0 0 0 0 0]
#     for i in range(n):  # 0~4
#         dp[i] = dp[i-1] + data[i]

#     final_data = []
#     for _ in range(m):  # m만큼, 0~2
#         i, j = map(int, sys.stdin.readline().split())  # 1 3
#         # i -= 1  # 0
#         # j -= 1  # 2
#         final_data.append(dp[j] - dp[i-1])  # dp[3] - dp[0] = 14 - 5 = 9

#     return final_data

# result = prefix_sum(data, n, m)
# for i in result:
#     print(i)
# -> final_data.append(dp[j] - dp[i-1]) IndexError: list index out of range
# dp를 n개 만들면 i=0일 때, dp[0]=dp[-1]+dp[0]이 되어버리기 때문에
# dp를 n+1개 만들어서 더해도 상관없는 0을 index 0번째에 두고 1부터 시작하면 됨.

import sys

n, m = map(int, sys.stdin.readline().split())  # 5 3 
data = list(map(int, sys.stdin.readline().split()))  # n개의 수만큼 입력, 5 4 3 2 1

def prefix_sum(data, n, m):
    dp = [0] * (n+1) 
    for i in range(1, n+1):  
        dp[i] = dp[i-1] + data[i-1]

    final_data = []
    for _ in range(m):  
        i, j = map(int, sys.stdin.readline().split()) 
        final_data.append(dp[j] - dp[i-1]) 

    return final_data

result = prefix_sum(data, n, m)
for i in result:
    print(i)