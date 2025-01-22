def generate_star_pattern(num):
    if num == 1:
        return ["*"]


    smaller_pattern = generate_star_pattern(num // 3)  # num을 3으로 나눈 작은 패턴 생성
    pattern = []

    for row in smaller_pattern:  # 첫 번째와 세 번째 부분
        pattern.append(row * 3)
    for row in smaller_pattern:  # 중간 부분: 가운데에 공백 추가
        pattern.append(row + " " * (num // 3) + row)
    for row in smaller_pattern:  # 첫 번째와 세 번째 부분 반복
        pattern.append(row * 3)

    return pattern



num = int(input())
result = generate_star_pattern(num)

print("\n".join(result))