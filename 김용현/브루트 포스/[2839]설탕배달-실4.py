n = int(input())

# 5kg 봉지만으로 정확히 나눠떨어지는 경우
if n % 5 == 0:
    print(n // 5)  # 5로 나눈 몫을 출력
else:
    p = 0  # 봉지 개수를 세는 변수
    while n > 0:
        n -= 3  # 먼저 3kg 봉지를 하나 사용
        p += 1  # 3kg 봉지 사용 개수 증가

        # 남은 무게가 5로 나눠떨어지는 경우
        if n % 5 == 0:
            p += n // 5  # 5kg 봉지 개수를 더함
            print(p)  # 총 봉지 개수 출력
            break

        # 1kg 또는 2kg이 남으면 더 이상 나눌 수 없음
        elif n == 1 or n == 2:
            print(-1)  # 정확히 나눌 수 없으므로 -1 출력
            break

        # 3으로 나눠떨어지는 경우
        elif n == 0:
            print(p)  # 총 봉지 개수 출력
            break