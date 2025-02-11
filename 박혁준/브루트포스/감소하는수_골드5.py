# 감소하는 수
# https://www.acmicpc.net/problem/1038
# 다른 사람 코드 참고해서 공부했습니다


from itertools import combinations

N = int(input())
result = []


for i in range(1, 11): 
    for temp in combinations(range(0, 10), i): 
    # 0부터 9까지 n개를 골라 순서를 고려하지 않고 선택 ex) i=3 -> 012 013 ...
        temp = list(temp)
        temp.sort(reverse=True)
        # 나온 수들을 뒤집음 -> 감소하는 
        result.append(int("".join(map(str, temp))))
        # 숫자로 변


result.sort()

try:
    print(result[N])
except:
    print(-1)