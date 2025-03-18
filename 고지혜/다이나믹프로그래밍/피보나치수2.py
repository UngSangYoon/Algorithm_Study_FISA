# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# n = int(input())
# print(fibonacci(n))
'''
f(5)=f(4)+f(3)
f(4)=f(3)+f(2)
f(3)=f(2)+f(1)
f(2)=f(1)+f(0)
-> 시간초과: 중복 계산 많아져서 실행 시간 길어짐
'''
# 반복문
def fibonacci(n):
    a = 0  # 첫번째
    b = 1  # 두번째
    for _ in range(n):
        a, b = b, a + b
    return a

n = int(input())
print(fibonacci(n))

'''
초기값:  a = 0,  b = 1
반복 1:  a   b
           a   b
반복 2:      a   b
반복 3:         a   b
반복 4:            a   b
반복 5:               a   b
'''