'''
#강의 듣기 전 풀이 -> 재귀로만 구현
n = int(input())

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
 
    return fibo(n-1) + fibo(n-2)

print(fibo(n))
# 중복된 계산을 하기 때문에 시간복잡도 O(2^n) 굉장히 오래 걸림
'''
# 중복 계산을 줄이자 -> 똑같은 값은 저장 -> 메모이제이션
def fibo(n):
    global arr
    
    if arr[n] != -1:
        return arr[n]
    
    arr[n] = fibo(n-1) + fibo(n-2)
    return arr[n]

n = int(input())
arr = [-1] * (n+1)
arr[0] = 0
arr[1] = 1
print(fibo(n))