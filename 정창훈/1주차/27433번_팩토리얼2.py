# GPT 활용해서 팩토리얼문 학습을 함
# 프롬프트를 12살도 이해할 수 있도록 설명해줘라고 하니 잘 설명해줌

def factorial(n):
    result = 1

    for i in range(1, n+1):
        result *= i
    return result

n = int(input("숫자 N 을 입력해주시오. (0 ≤ N ≤ 20): "))

factorial_result = factorial(n)

print(factorial_result)
