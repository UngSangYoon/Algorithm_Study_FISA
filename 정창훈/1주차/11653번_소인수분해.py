N = int(input("소인수분해할 숫자를 입력하세요: "))

# 소인수분해
if N > 1:  # 1은 소인수가 없으므로 처리하지 않음
    factor = 2  # 가장 작은 소수 2부터 시작
    while N > 1:  # N이 1이 될 때까지 반복
        if N % factor == 0:  # N이 factor로 나누어떨어지면
            print(factor)  # factor를 출력
            N = N // factor  # N을 factor로 나눈 값으로 업데이트
        else:
            factor += 1  # 나누어떨어지지 않으면 다음 숫자로 이동
