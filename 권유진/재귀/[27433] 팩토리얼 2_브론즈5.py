'''
문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 20)이 주어진다.

출력
첫째 줄에 N!을 출력한다.

예제 입력 1 
10

예제 출력 1 
3628800
'''

def factorial(n):
    if n<2: 
        return 1
    return n*factorial(n-1)

print(factorial(int(input())))
