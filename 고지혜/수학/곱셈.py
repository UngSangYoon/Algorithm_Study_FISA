'''
문제
자연수 A를 B번 곱한 수를 알고 싶다. 
단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. 
A, B, C는 모두 2,147,483,647 이하의 자연수이다.
출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

ex.
입력 > 10 11 12
출력 > 4
'''

def div_func(a, b, c):
    result = 1
    for i in range(b):  # b번 반복
        result = (result * a) % c

    return result
    
a, b, c = map(int, input().split())
print(div_func(a, b, c))  # output


# a=10 b=11 c=12
# result = (1x10)%12 = 10
# result = (10x10)%12 = 4
# result = (4x10)%12 = 4
# .. 반복 -> 4 

# def modular_exponentiation(a, b, c):
#     # Base case: b == 0
#     if b == 0:
#         return 1

#     # Divide and conquer
#     half = modular_exponentiation(a, b // 2, c)
#     half = (half * half) % c

#     # If b is odd, multiply one more 'a'
#     if b % 2 == 1:
#         half = (half * a) % c

#     return half