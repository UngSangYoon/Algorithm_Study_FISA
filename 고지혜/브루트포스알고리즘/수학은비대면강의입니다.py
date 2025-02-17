# 1. 
# 첫번째 방정식을 d배, 두번째 방정식 a배 해서 x계수 먼저 맞추기
# (b*d)y - (a*e)y = c*d - a*f
# ax = c - by
# a, b, c, d, e, f = map(int, input().split())

# # 런타임 에러 (ZeroDivisionError) -> 분모가 0인 경우 모두 고려해야함
# y = (c * d - a * f) // (b * d - a * e)
# x =  (c - b * y) // a

# print(x, y)
# -------------------모든 경우 고려하기-------------------
# 2.
# a, b, c, d, e, f = map(int, input().split())

#  x를 제거하고 y를 구하는 경우
# if a == 0 and d == 0:  # x 항이 없는 경우
#     y = c // b
#     if e * y == f:
#         print(0, y)
#     else:
#         exit()

# elif b == 0 and e == 0:  # y 항이 없는 경우
#     x = c // a
#     if d * x == f:
#         print(x, 0)
#     else:
#         exit()

# elif a == 0:  # x가 없는 경우, y를 먼저 구함
#     y = c // b
#     x = (f - e * y) // d
#     print(x, y)

# elif d == 0:  # x가 없는 경우, y를 먼저 구함
#     y = f // e
#     x = (c - b * y) // a
#     print(x, y)

# else:
#     # 일반적인 소거법 적용
#     y = (c * d - a * f) // (b * d - a * e)
#     x = (c - b * y) // a
#     print(x, y)

# --------------------------------------------------------

a, b, c, d, e, f = map(int, input().split())

# 완전 탐색 
# a~f: -999 이상 999 이하
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            exit()
