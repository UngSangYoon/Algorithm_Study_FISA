'''
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
'''

n = int(input())
numbers = list(map(int, input().split()))
cnt = 0

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

for num in numbers:
    if is_prime(num):
        cnt += 1

print(cnt)

'''
3부터 소수인지 아닌지 루트 n만큼 반복하여 찾도록 구현하였습니다.
'''