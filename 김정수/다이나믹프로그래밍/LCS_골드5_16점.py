'''
LCS - 골드5 - 16점

LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
'''


X = input()
Y = input()

n,m = len(X), len(Y)

dp = [
    [0 for _ in range(m+1)]
    for _ in range(n+1)
]

# 인덱스 에러를 피하기 위해 X와 Y의 맨 앞에 아무 문자나 추가
X, Y = '#'+X, '#'+Y

def LCS(X,Y):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if X[i] == Y[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]


print(LCS(X,Y))