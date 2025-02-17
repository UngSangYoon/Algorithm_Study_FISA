'''
문제
베라는 상의 N 벌과 하의 N 벌이 있다. i 번째 상의와 i 번째 하의는 모두 색상 i를 가진다. N 개의 색상은 모두 서로 다르다.

상의와 하의가 서로 다른 색상인 조합은 총 몇 가지일까?

입력
입력은 아래와 같이 주어진다.

N
출력
상의와 하의가 서로 다른 색상인 조합의 가짓수를 출력한다.

제한
1 ≤ N ≤ 2017
N은 정수이다.
예제 입력 1 
1
예제 출력 1 
0
'''

from itertools import permutations

N=int(input())

Nlist=[i for i in range(1,N+1)]

cnt=0

for i in permutations(Nlist,2):
    if i[0]!=i[1]:
        cnt+=1

print(cnt)

