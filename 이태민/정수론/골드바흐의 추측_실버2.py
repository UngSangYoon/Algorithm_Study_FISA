# 9020번
# 골드바후 추측 -> 2보다 큰 모든 짝수는 두 소수의 합으로 표현 가능할 것
# 골드바흐 파티션 -> 짝수를 소수 2개의 합으로 표현

# 1. 입력받은 수 보다 작은 모든 소수를 찾는다.
# 1-1. 소수는 약수가 2개인 것을 의미한다.
# 1-2. 그럼 약수를 구하는 함수를 우선 만든다.
# 1-3. 약수의 개수가 2개이면 소수다.


# 첫 번째 풀이

# # 소수 찾기 -> 약수가 2개
# import math

# # 약수 함수
# def get_division(n):
#     set_ = set()
#     for i in range(1, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             set_.add(i)
#             set_.add(n // i)
#     return set_

# # 소수 찾기
# def is_prime(n):
#     return (len(get_division(n)) == 2)

# # 입력 받은 수보다 작은 모든 소수를 찾는다.
# def find_prime(n):
#     n = n - 2
#     li_ = [True] * n
#     li_[0] = False
#     for i in range(2, n + 1):
#         if is_prime(i):
#             continue
#         else:
#             li_[i-1] = False
#     return [idx + 1 if value else value for idx, value in enumerate(li_)]

# iter_ = int(input())
# for it in range(iter_):
#     num = int(input())
#     print(*sorted(find_prime(num))[-2:])


def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

n = int(input())

for _ in range(n):
    num = int(input())
    
    a, b = num//2, num//2

    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1