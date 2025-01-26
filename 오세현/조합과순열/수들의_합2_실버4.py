"""
백준 2003번 수들의 합2 실버4
문제
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다.
"""

"""
# N개의 수의 합 == M 을 만족하는 경우의 수를 출력하기
# 단, 무작정 뽑지 않고, 연속된 인덱스 번호로 뽑아야 함


# 처음에 아래와 같이 라이브러리 사용해서 풀었는데, 조합을 중복으로 저장하는 문제 발생함
"""
# N과 M값 입력받기
n, m = map(int, input().split())

# 수열 a에 N개의 수 입력받기
a = list(map(int, input().split()))

# 경우의 수를 저장할 변수
c = 0

# 수열 a에서 1이상 N이하의 개수만큼 뽑아 리스트에 저장
for i in range(1, n+1):
    aPi = list(itertools.permutations(a, i))

    for j in range(len(aPi)):
        # 리스트 aPi의 원소 중, 원소 합이 m을 만족할 경우 c += 1
        if sum(aPi[j]) == m:
            print(aPi[j])
            c += 1
    
    del aPi[:]
    

print(c)

"""
# 두 번째 시도 코드 -> 시간 초과
# 실패 원인: 수열의 모든 조합을 브루트포스로 탐색하고 있어 실행 시간이 N^2이상으로 매우 큼

# 수열 a의 원소 중 인덱스 번호 i부터 j까지의 합(sum(a[i:j])이 m인 조합 찾아내기

i = 0, j = 1, 2, 3, 4
i = 1, j = 2, 3, 4
i = 2, j = 3, 4
i = 3, j = 4

즉, for문을 아래와 같이 작성할 수 있음
i의 범위는 0부터 n-1 까지
j의 범위는 i+1 부터 n 까지

n, m = map(int, input().split())
a = list(map(int, input().split()))

c = 0

for i in range(n):
    for j in range(i+1, n+1):
        if sum(a[i:j]) == m:
            c += 1      # 조건 만족 시, 경우의 수 += 1

print(c)
"""

# 최종 제출 코드
n, m = map(int, input().split())

a = list(map(int, input().split()))

# 필요한 변수 선언
start = 0
end = 0
count = 0

sum = a[0]

while True:
    # sum이 m과 동일한 경우, count += 1
    if sum == m:
        count += 1

    # sum이 m 이상일 경우
    if sum >= m:
        # start 1 올리고, sum 초기화
        start += 1
        sum -= a[start-1]
        
    # sum이 m 미만인 경우    
    else:    
        # end 값이 마지막 인덱스 번호와 같다면, 반복 중지
        if end == n - 1:
            break
        
        # end 1 올리고 sum에 값 더하기
        end += 1
        sum += a[end]

print(count)

"""
이중 for문을 사용했던 두 번째 코드와 달리, 
start와 end가 각각 한 방향으로만 이동하기 때문에 훨씬 효율적임

"""