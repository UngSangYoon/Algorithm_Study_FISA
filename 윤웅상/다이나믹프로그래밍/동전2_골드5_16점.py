'''
문제
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 
각각의 동전은 몇 개라도 사용할 수 있다.

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다. 
가치가 같은 동전이 여러 번 주어질 수도 있다.

출력
첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.

예제 입력 1 
3 15
1
5
12
예제 출력 1 
3
'''
# 그리디 큰 수만을 선택 -> 작은 수를 선택할 떄 더 큰 수를 만들 수 있음
'''
n, k = map(int, input().split())
v_list = []
for _ in range(n):
    v = int(input())
    if v <= k:
        v_list.append(v)
if v_list == []:
    print("-1")

else:    
    dp = [0] * (k+1)
    for v in v_list:
        dp[v] += 1

    cnt = 0
    while k != 0:
        for i in range(k,-1,-1):
            if i == 0:
                k = 0

            if dp[i] > 0:
                dp[i] -= 1
                k -= i
                cnt += 1
                break
            
    if cnt == 0:
        cnt = -1
    print(cnt)
'''

# DP -> k 이하의 최대값으로 문제를 잘못 이해
'''
n, k = map(int, input().split())
v_list = []
for _ in range(n):
    v = int(input())
    if v <= k:
        v_list.append(v)
v_list.sort(reverse = True)
if v_list == []:
    print('-1')
# 2차원 DP
# 각 행은 동전의 종류
# 각 열은 동전의 사용 개수
# DP의 값은 해당 동전을 그 개수만큼 사용하였을 때 최대값 
# ex) vlist : [8, 5, 1] k=10
#      0  1  2  3  4  5  6  7  8  9  10
# 8:  [0  8 -1 -1 -1 -1 -1 -1 -1 -1  -1]
# 5:  [8  5 10 -1 -1 -1 -1 -1 -1 -1  -1]
# 1:  [10 9 10  8  9 10  6  7  8  9  10]
else:
    m = k//v_list[-1]
    dp = [[(-1,0)]*(m) for _ in range(n)]
    dp[0][0] = (0,0)
    for i in range(1, m):
        if v_list[0]*i <= k:
            dp[0][i] = (v_list[0] * i, i)
        else:
            break

    for type in range(1, n):
        for count in range(k):
            for i in range(m-1,-1,-1):
                if dp[type-1][i][0] == -1:
                    continue
                else:
                    if dp[type-1][i][0] + (v_list[type] * count) <= k:
                        dp[type][count] = (dp[type-1][i][0] + (v_list[type] * count), count+dp[type-1][i][1])
                        break

    def find_max_min(points):
        max_x = max(points, key=lambda p: p[0])[0]  # 가장 큰 x 값 찾기
        candidates = [p for p in points if p[0] == max_x]  # x가 최대인 요소들 필터링
        return min(candidates, key=lambda p: p[1])  # y 값이 최소인 요소 찾기

    print(find_max_min(dp[-1])[1])
    ''' 
# 입력 받기
n, k = map(int, input().split())
v_list = []
for _ in range(n):
    v = int(input())
    if v <= k:  # k보다 큰 동전은 사용할 수 없으므로 제외
        v_list.append(v)

# 동전이 없거나 유효한 동전이 없는 경우
if not v_list:
    print(-1)
else:
    # DP 테이블 초기화
    # dp[j]는 금액 j원을 만들기 위해 필요한 최소 동전 개수
    dp = [float('inf')] * (k + 1)
    dp[0] = 0

    # 각 동전에 대해 DP 갱신
    for coin in v_list:
        for j in range(coin, k + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    # 결과 출력
    if dp[k] == float('inf'):
        print(-1)
    else:
        print(dp[k])