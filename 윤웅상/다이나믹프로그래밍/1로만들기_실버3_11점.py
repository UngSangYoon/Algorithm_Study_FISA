'''
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
'''
# 그리디 문제풀이 -> 항상 3으로 나누는 것이 가장 빠른 길이 아님
'''
X = int(input())

def recur(n, cnt):
    if n == 1:
        return cnt 
    
    elif n % 3 == 0:
        result = recur(n//3, cnt+1)

    elif n % 2 == 0:
        result = recur(n//2, cnt+1)
    else:
        result = recur(n-1, cnt+1)
    return result

print(recur(X, 0))'
'''
'''
# dp top-down 방식 풀이

X = int(input())
dp = [float('inf')] * (X+1)

def recur(n, cnt):
    if n == 1:
        dp[n] = min(dp[n], cnt)
        return
    else:
        if n%3==0:
            if dp[n//3] <= cnt + 1:
                return
            else:
                dp[n//3] = cnt + 1
                recur(n//3, cnt + 1)

        if n%2==0:
            if dp[n//2] <= cnt + 1:
                return
            else:
                dp[n//2] = cnt + 1
                recur(n//2, cnt + 1)
        if dp[n-1] <= cnt + 1:
            return
        else:
            dp[n-1] = cnt + 1
            recur(n-1, cnt + 1)

recur(X,0)
print(dp[1])
'''
# 바텀업 방식의 풀이
X = int(input())
dp = [0] * (X + 1)  # dp[i]는 i를 1로 만드는 최소 연산 횟수

for i in range(2, X + 1):
    dp[i] = dp[i - 1] + 1  # 1을 빼는 연산
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)  # 2로 나누는 연산
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)  # 3으로 나누는 연산

print(dp[X])