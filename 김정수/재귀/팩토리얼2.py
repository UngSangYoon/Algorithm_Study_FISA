팩토리얼2

'''
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
'''

n = int(input())


def facto(n):
    if n < 1:
        return 1
    else:
        return facto(n-1) * n

ans = facto(n)

print(ans)