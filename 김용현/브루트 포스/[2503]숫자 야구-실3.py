from itertools import permutations


def count_possible_answers(conditions):

    answer_count = 0

    # 모든 가능한 3자리 숫자 조합을 생성
    for candidate in permutations(range(1, 10), 3):
        # 플레그 - true 로 설정
        is_valid = True

        # 각 조건에 대해 후보가 조건을 만족하는지 확인
        for number, strike, ball in conditions:
            strike_count = 0
            ball_count = 0

            # 스트라이크와 볼 개수 계산
            # 문자열이기 때문에 정수화 시켜주기
            for i in range(3):
                if candidate[i] == int(number[i]):
                    strike_count += 1
                elif candidate[i] in map(int, number):
                    ball_count += 1

            # 조건과 일치하지 않으면 후보 탈락
            if strike_count != int(strike) or ball_count != int(ball):
                is_valid = False
                break

        # 모든 조건을 만족하면 유효한 정답 후보
        if is_valid:
            answer_count += 1

    return answer_count



n = int(input())
conditions = [input().split() for _ in range(n)]


print(count_possible_answers(conditions))