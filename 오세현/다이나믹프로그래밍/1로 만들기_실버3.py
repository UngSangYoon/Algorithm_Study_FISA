"""
백준 1463번 1로 만들기 실버3

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
"""

# 정수 n 입력받기
n = int(input())

"""
Bottom-Up 방식으로 풀기
- 작은 문제부터 차례대로 계산해 올라가는 방법

"""

# 초기 리스트 생성
dp = [0] * (n + 1)

# 1부터 n까지 최소 연산 횟수 계산
for i in range(2, n + 1):
    # 기본적으로 이전 숫자에서 1을 뺀 경우
    dp[i] = dp[i - 1] + 1
    # 2로 나누어 떨어질 경우 최소값 갱신
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 3으로 나누어 떨어질 경우 최소값 갱신
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

# 결과 출력
print(dp[n])
