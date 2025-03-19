'''
구간 합 구하기 4 - 실버3 - 11

수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
'''


n, m = map(int, input().split())
li = list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = dp[i-1] + li[i-1]

ans = 0
ans_li = []
for i in range(m):
    a,b = map(int, input().split())
    ans = dp[b] - dp[a-1]
    ans_li.append(ans)


for elem in ans_li:
    print(elem)

'''
보니까 dp 테이블은 dp[i-1]과 input으로 주어진 리스트 li[i-1]을 더한 것으로 채우고,
정답인 구간의 합은 '끝리스트인덱스'와 '시작리스트인덱스-1'를 빼면 나왔습니다.
'''