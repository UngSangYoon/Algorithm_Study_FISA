'''
문제
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만, {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.
'''

n = int(input())
lst = list(map(int, input().split()))

dp = [1] * n
# dp[i]는 lst[i]가 가장 중간 수인 경우
dp_sub = [0] * n

  # 증가하는 부분
for i in range(n):
  for j in range(i):
    if lst[i] > lst[j]:
      dp[i] = max(dp[i], dp[j]+1)

  # 감소하는 부분
for i in range(n-2, -1, -1):
  for j in range(i+1, n):
    if lst[i] > lst[j]:
      dp_sub[i] = max(dp_sub[i], dp_sub[j]+1)

result = [dp[i] + dp_sub[i] for i in range(len(dp))]
print(max(result))
