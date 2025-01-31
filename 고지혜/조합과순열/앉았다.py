from itertools import combinations

def get_rank(a, b):
    if a == b:
        # return (a, '땡')  # -> 1 1 입력시, 0.183 나오는 이유
        # => (1, 1)과 (9, 0)을 비교하면 
        # 첫번째 요소 비교에서 1 vs 9에서 9가 커서 더 높은것으로 잘못 판별(단순 숫자 비교)
        # 따라서 땡을 높게 처리하기 위해 더 큰 값으로 변환시키기
        return (a + 10, 1)  
    # return ((a + b) % 10, '끗')  # 한자리면 그냥 나오지만, 두자리수는 나머지로 보면 됨
    return ((a + b) % 10, 0)

def cal(a, b):
    # 카드 준비 - 1~10이 2장씩 존재
    all_card = [i for i in range(1, 11)] * 2
    # 겹치면 안되니까
    all_card.remove(a)  
    all_card.remove(b)

    # 영학이
    younghak = get_rank(a, b)

    total = 0
    win = 0

    for i, j in combinations(all_card, 2):
        option = get_rank(i, j)  # 상대방
        total += 1

        if younghak > option:
            win += 1
        
    win_ = round(win / total, 3)
    return f'{win_:.3f}'  # 소수점 3자리 고정 출력
    
# 입력
a, b = map(int, input().split())
print(cal(a, b))