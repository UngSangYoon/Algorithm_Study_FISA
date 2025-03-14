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

예제 입력 2 
0
예제 출력 2 
1
'''

n = int(input())
result = 1 
for i in range(n, 0, -1):
    result *= i

print(result)

'''
def recur(num):
    if num == 1:
        return 1
    return num * recur(num-1)

print(recur(n))
'''