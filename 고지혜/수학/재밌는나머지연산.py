'''
문제
정수N을 m으로 나눈 나머지가 R이되도록 하는 모든 양의 정수 m의 합 구하기

입력
첫째줄에 정수N과 R이 공백을 사이에 두고 주어진다(1<=N<=10^12, 0<=R<N)
출력 
정수N을 M으로 나눈 나머지가 R이 되도록 하는 모든 양의 정수m의 합 출력한다. 조건을 만족하는 m이 없으면 0 출력한다.

ex.
입력 > 16 4
출력 > 18
'''
def sum_of_valid_m(n, r):
    if r >= n:
        return 0  # 조건을 만족하는 M이 없음

    target = n - r  # m은 n-r의 약수여야 함.
    m_sum = 0

    # 약수 구하기 (√target까지 탐색)
    for i in range(1, int(target**0.5) + 1):  # 
        if target % i == 0:
            # i와 target // i가 약수
            if i > r:  # 약수 i가 m>r 만족하는지.
                m_sum += i
            # 약수 i가 target//i와 같지 않은지(중복 방지), target//i도 약수이므로 m에 포함될 수 o
            if (target // i != i) and (target // i > r):
                m_sum += target // i

    return m_sum  # m의 합 반환

# 입력 받기
n, r = map(int, input().split())
print(sum_of_valid_m(n, r))
