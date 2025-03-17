'''
오른쪽 그림과 같이 삼각형이 나선 모양으로 놓여져 있다. 첫 삼각형은 정삼각형으로 변의 길이는 1이다. 그 다음에는 다음과 같은 과정으로 정삼각형을 계속 추가한다. 나선에서 가장 긴 변의 길이를 k라 했을 때, 그 변에 길이가 k인 정삼각형을 추가한다.

파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다. P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다.

N이 주어졌을 때, P(N)을 구하는 프로그램을 작성하시오.
'''


T = int(input())

ans_li = []

for i in range(T):
    ans_num = int(input())
    ans_li.append(ans_num)


dp = [0] * max(ans_li)
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 3
dp[6] = 4

n = max(ans_li)

for i in range(7, n):
    dp[i] = dp[i-1] + dp[i-5]


for ele in ans_li:
    print(dp[ele-1])


'''
보니까 인덱스 7부터 i = (i-1) + (i-5)였습니다.
'''