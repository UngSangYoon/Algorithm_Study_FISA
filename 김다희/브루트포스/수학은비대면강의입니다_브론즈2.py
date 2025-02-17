import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())
x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)
print(x, y)


# 2. 브루트포스: 시간 초과
# import sys
# input = sys.stdin.readline

# a, b, c, d, e, f = map(int, input().split())
# for x in range(-999, 1000):
#     for y in range(-999, 1000):
#         if (a*x + b*y == c) & (d*x + e*y == f):
#             print(x, y)
#             sys.exit(0)


# 3. 
# import sys
# input = sys.stdin.readline
# a, b, c, d, e, f = map(int, input().split())
# y = (c*d - f*a)/(b*d - e*a)
# x = (c - b*y)/a
# print(int(x), int(y))

# 4. 
# import sys
# input = sys.stdin.readline
# a, b, c, d, e, f = map(int, input().split())
# y = (c-(f*a)/d)//(b-(e*a)/d)
# x = (c-b*y)//a
# print(int(x), int(y))