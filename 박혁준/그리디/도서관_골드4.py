def solution(list_):
    list_sorted = sorted(list_)  # 리스트 정렬
    
    # 음수와 양수 리스트 나누기
    negative = [x for x in list_sorted if x < 0]
    positive = [x for x in list_sorted if x >= 0]

    # 특정 조건에 따라 값을 더하는 함수
    def foot_sum(li_):
        li_abs = [abs(x) for x in li_]  # 절대값 리스트
        li_len = len(li_abs)

        if li_len % 2 == 1:  # 홀수 개수라면 짝수 인덱스(0, 2, 4...)의 합
            return sum(li_abs[i] for i in range(0, li_len, 2))
        else:  # 짝수 개수라면 홀수 인덱스(1, 3, 5...)의 합
            return sum(li_abs[i] for i in range(1, li_len, 2))

    # 음수 리스트와 양수 리스트 각각 계산 후 합산
    return foot_sum(negative) + foot_sum(positive)

# 입력 받기
n, k = map(int, input().split())
list_ = list(map(int, input().split()))

# 결과 출력
print(solution(list_))
