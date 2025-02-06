# 1. input(), 40ns
# n = int(input())  # 선수 수
# players = []

# # 선수 등번호, 종목별 순위 입력 받기
# for _ in range(n):
#     # b: 등번호, q: 리드, q: 스피드, r: 볼더링
#     b, p, q, r = map(int, input().split())
#     scores = p * q * r  # 점수: 리드*스피드*볼더링 순위
#     scores_sum = p + q + r  # 동점인 경우 합산 점수가 낮은 선수 판단 시 사용

#     players.append((scores, scores_sum, b))  # (점수, 순위합, 등번호) 튜플로 추가

# # 정렬: 1)점수 오름차순, 2)순위 합 오름차순, 3)등번호 오름차순
# players.sort(key=lambda x : (x[0], x[1], x[2]))

# # print(players)  # >> [(4, 5, 815), (4, 6, 717), (24, 9, 301), (24, 9, 505)]
# # 금, 은, 동 순으로 등번호 출력
# print(players[0][2], players[1][2], players[2][2])

# -------------------------------------------------------------------------------

# 2. readline(), 36ms
import sys

n = int(sys.stdin.readline())  # 모든 줄 한 벙네 리스트에 저장
players = []

# 선수 등번호, 종목별 순위 입력 받기
for _ in range(n): 
    b, p, q, r = map(int, sys.stdin.readline().split())  # 등번호, 리드, 스피드, 볼더링 순
    scores = p * q * r  # 점수: 리드*스피드*볼더링 순위
    scores_sum = p + q + r  # 동점인 경우 합산 점수가 낮은 선수 판단 시 사용

    players.append((scores, scores_sum, b))  # (점수, 순위합, 등번호) 튜플로 추가

# 정렬: 1)점수 오름차순, 2)순위 합 오름차순, 3)등번호 오름차순
players.sort(key=lambda x : (x[0], x[1], x[2]))

# print(players)  # >> [(4, 5, 815), (4, 6, 717), (24, 9, 301), (24, 9, 505)]
# 금, 은, 동 순으로 등번호 출력 (3가지)
# print(players[0][2], players[1][2], players[2][2])

# for i in range(3): 
#     print(players[i][2], end=' ')  # 공백으로 구분

print(' '.join(str(players[i][2]) for i in range(3)))