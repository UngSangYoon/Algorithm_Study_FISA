def min_coins(change):
    coins = [500, 100, 50, 10, 5, 1]
    count = 0
    
    for coin in coins:
        count += change // coin  # 해당 동전으로 거슬러 줄 수 있는 개수
        change %= coin  # 나머지 금액 업데이트
    
    return count

# 입력 받기
price = int(input())
change = 1000 - price
print(min_coins(change))
