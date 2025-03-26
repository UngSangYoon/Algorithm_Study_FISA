# 최대 N 값에 대해 미리 파도반 수열 계산
P = [0] * 101  # 최대 100까지 필요한 파도반 수열

# 초기값 설정
P[1] = P[2] = P[3] = 1

# 파도반 수열 계산
for i in range(4, 101):
    P[i] = P[i-2] + P[i-3]

# 테스트 케이스 입력
T = int(input())  # 테스트 케이스 수

# 각 테스트 케이스에 대해 P(N) 출력
for _ in range(T):
    N = int(input())
    print(P[N])
