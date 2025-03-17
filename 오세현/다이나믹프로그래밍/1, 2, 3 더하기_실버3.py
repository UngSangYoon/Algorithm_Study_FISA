"""
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

"""


# 가능한 조합의 수를 세는 함수 정의
def count_comb(n, current_sum):     
    # 현재 합이 n과 같으면 조합을 하나 찾은 것
    if current_sum == n:
        return 1
    # 현재 합이 n을 초과하면 무효한 조합
    if current_sum > n:
        return 0
    
    # 1, 2, 3을 각각 더하는 모든 조합을 탐색
    return (
        count_comb(n, current_sum + 1) +
        count_comb(n, current_sum + 2) +
        count_comb(n, current_sum + 3)
    )

# 테스트 케이스 처리
t = int(input())  # 테스트 케이스 개수 입력
for _ in range(t):
    n = int(input())
    print(count_comb(n, 0))



