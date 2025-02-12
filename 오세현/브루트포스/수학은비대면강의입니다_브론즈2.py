# 백준 19532번 수학은 비대면강의입니다 브론즈2

# a부터 e까지 입력받기
a, b, c, d, e, f = map(int, input().split())


# a, b, c, d 모두 같으면 0
if (a == d) & (b == e):
    x, y =0

elif (a == d) & (b != e):
    #((b - e) * y) = c - f
    y = (c - f) / (b - e)
    #a * x + b * y = c
    x = (c - (b * y)) / a

elif (a != d) & (b == e):
    # ((a - d) * x) = c - f
    x = (c - f) / (a - d)
    #a * x + b * y = c
    y = (c - (a * x)) / b

else:
    # 최소공배수 구하기 귀찮.. 대신 1로 만들자
    """
    a * x + b * y = c
    x + (b / a) * y = (c / a)
    x + (e / d) * y = (f / d)
    ((b / a) - (e / d)) * y = (c / a) - (f / d)
    """
    y = ((c / a) - (f / d)) / ((b / a) - (e / d))

    # 오류: ((b / a) - (e / d)) 이 값이 0일 가능성 존재
    x = (c - (b * y)) / a

print(int(x), int(y))



# 완전 탐색법
# 입력 받기
a, b, c, d, e, f = map(int, input().split())

# 완전 탐색으로 해를 찾기
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a * x + b * y == c) and (d * x + e * y == f):
            print(x, y)
            exit()  # 정답을 찾으면 즉시 종료

