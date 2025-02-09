# 5킬로그램 봉지 먼저 사용
# 남은 무게 3으로 나눠지면 3킬로그램 봉지로
# 3으로 나누어떨어지지 않으면 -1 출력
def sugar_delivery(n):
    for i in range(n // 5, -1, -1):  # -1로 내려가면서 봉지 개수 줄이기
        count_5kg = n - (5 * i)  # 5kg i개 사용 후 남은 설탕
        if count_5kg % 3 == 0:  # 3으로 나눠지면
            return i + (count_5kg // 3)  # 봉지 개수 더해서 반환하기
    return -1  # 나누어떨어지지 않으면 -1 반환

n = int(input())
print(sugar_delivery(n))