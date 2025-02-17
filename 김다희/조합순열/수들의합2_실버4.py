# 투 포인터, O(N)
# 2개의 포인터를 활용하여, 부분합 구하고 조건에 만족하는 경우 카운트
# r: 오른쪽, l: 왼쪽 인덱스 위치
n, m = map(int, input().split())
a = list(map(int, input().split()))
r = 0; l = 0; asum = 0; k = 0

while r < n: # 오른쪽 인덱스 위치가 리스트 내일 때
    asum = asum + a[r] # 합에 오른쪽 인덱스의 값 추가
    r = r+1 # 오른쪽으로 한 칸 더 이동

    while (asum > m) and (l < r): # 합이 m보다 크고, 오른쪽 인덱스 전까지
        asum = asum - a[l] # 합에서 왼쪽 값 빼기
        l = l+1 # 오른쪽으로 한 칸 더 이동
    
    if asum == m:
        k = k+1

print(k)



# 아래는 재귀를 사용한 코드
# 시간복잡도가 O(N^2)로 런타임에러 발생... 
# >> 투 포인터 기법 적용 필요, O(N)
'''
n, m = map(int, input().split())
a = list(map(int, input().split()))
k = 0

def com(index, total):
    global k

    if total == m:
        k = k+1
        return
    
    if (total > m) or (index >= n):
        return
    
    com(index+1, total+a[index])

for i in range(n):
    com(i, 0)

print(k)
'''