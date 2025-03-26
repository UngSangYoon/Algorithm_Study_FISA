'''
스티커 - 실버1 - 15점

상근이의 여동생 상냥이는 문방구에서 스티커 2n개를 구매했다. 스티커는 그림 (a)와 같이 2행 n열로 배치되어 있다. 상냥이는 스티커를 이용해 책상을 꾸미려고 한다.

상냥이가 구매한 스티커의 품질은 매우 좋지 않다. 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다. 즉, 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.

모든 스티커를 붙일 수 없게된 상냥이는 각 스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어내려고 한다. 먼저, 그림 (b)와 같이 각 스티커에 점수를 매겼다. 상냥이가 뗄 수 있는 스티커의 점수의 최댓값을 구하는 프로그램을 작성하시오. 즉, 2n개의 스티커 중에서 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합을 구해야 한다.

위의 그림의 경우에 점수가 50, 50, 100, 60인 스티커를 고르면, 점수는 260이 되고 이 것이 최대 점수이다. 가장 높
'''


T = int(input())

for _ in range(T):
    n = int(input())

    upper = list(map(int, input().split()))
    lower = list(map(int, input().split()))

    table = []

    table.append(upper)
    table.append(lower)


    dp = [[0] * n for _ in range(2)]

    if n == 1:
        if table[0] > table[1]:
            print(table[0][0])
        else:
            print(table[1][0])
    elif n == 2:
        a = table[0][0] + table[1][1]
        b = table[1][0] + table[0][1]
        if a > b:
            print(a)
        else:
            print(b)
    else:
        dp[0][0] = table[0][0]
        dp[0][1] = table[1][0] + table[0][1]
        dp[1][0] = table[1][0]
        dp[1][1] = table[0][0] + table[1][1]

        ans = []

        for j in range(2,n):
            dp[0][j] = max(dp[1][j-2], dp[1][j-1], dp[0][j-2]) + table[0][j]
            ans.append(dp[0][j])

            dp[1][j] = max(dp[0][j-2], dp[0][j-1], dp[1][j-2]) + table[1][j]
            ans.append(dp[1][j])

        print(max(ans))



'''
다른 사람들 풀이 보니까 제가 유독 좀 더럽게 푼거 같긴 한데 좀 더 접근하기 쉬운 방법이지 않을까 싶습니다.
저는 점화식을 아래와 같이 도출해냈습니다.

dp[0][j] = max(dp[1][j-2], dp[1][j-1], dp[0][j-2]) + table[0][j]
dp[1][j] = max(dp[0][j-2], dp[0][j-1], dp[1][j-2]) + table[1][j]

식으로 보면 복잡해 보이지만 테이블 그림을 그려서 보면 굉장히 이해하기 쉽습니다.
저는 자꾸 indexError와 valueError가 나왔는데, 그 이유는 n=1인 경우와 n=2인 경우 예외 처리를 안했기 때문이었습니다.
'''