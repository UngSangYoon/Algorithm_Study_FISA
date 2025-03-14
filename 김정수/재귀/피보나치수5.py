피보나치수5

'''
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
'''

n = int(input())

arr = [-1]*(n+2)
arr[0]=0
arr[1]=1

def fibo(x):
    global arr

    if arr[x] != -1:
        return arr[x]

    arr[x] = fibo(x-1) + fibo(x-2)
    return arr[x]


print(fibo(n))


'''
시간 복잡도가 위 코드에 비해 길지만 쉬운 코드입니다.

n = int(input())

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(n))

'''