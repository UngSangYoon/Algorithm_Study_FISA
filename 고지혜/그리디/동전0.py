'''
< 동전 n개 최소화해서 k원 만들기 >
# 동전 가치는 앞 동전의 배수
1. 큰 가치 동전 먼저
2. 동전 개수 계산 (몫)
3. 나머지 값 갱신
'''
def min_coin(n, k, coins):
    count = 0  # 동전 개수 초기화
    for coin in reversed(coins):
        # print(coin)
        if k == 0:
            break
        count = count + k // coin  # 동전개수 누적, 최대 몇개 사용할 수 있는지
        k = k % coin  # 남은 금액
        # print(count, k)
    return count


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]  # n개만큼
print(min_coin(n, k, coins))

'''
5000, 4200//5000=0, 4200%5000=4200=k -> 0+0
1000, 4200//1000=4, 4200%1000=200=k -> 0+4=4
500, 200//500=0, 200%500=200=k -> 4+0=4
20, 200//20=10, 200%10=0=k break -> 4+10=14개
1
'''