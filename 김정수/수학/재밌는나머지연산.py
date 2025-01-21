'''
정수 N을 m으로 나눈 나머지가 R이 되도록 하는 모든 양의 정수 m의 합을 구하라.
'''

N, R = map(int, input().split())
X = N - R  # N - R

# 1. 예외 케이스: R >= N
if R >= N:
    print(0)

# 2. 예외 케이스: X == 0 (N == R)
if X == 0:
    print(0)

total_sum = 0
i = 1
# 3. 1부터 sqrt(X)까지의 약수를 찾는다
while i * i <= X:
    if X % i == 0:  # i가 X의 약수라면
        # (1) i가 R보다 큰지 체크
        if i > R:
            total_sum += i

        # (2) X // i 가 i와 다른 약수일 때
        other = X // i
        if other != i and other > R:
            total_sum += other

    i += 1

print(total_sum)


'''
시간 초과로 꽤나 고생을 했는데 N = k x m + R이라는 수식에서
N - R = k x m => 나머지 정리에 의해 R은 언제나 0 <= R <= m을 만족해야 한다는 성질을 통해
m > R을 만족시키는 N - R의 모든 양의 약수의 합으로 풀었습니다.
'''