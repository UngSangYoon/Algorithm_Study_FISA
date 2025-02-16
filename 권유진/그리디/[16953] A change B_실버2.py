'''
문제
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

입력
첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

출력
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

예제 입력 1 
2 162
예제 출력 1 
5
'''

# A-> B
A,B=map(int,input().split())

answer=0
num=set()
num.add(A)

while len(num):
    if B in num:
        print(answer+1)
        break
    else :
        num_tmp=set()
        for i in num:
            if i*2 <= B:
                num_tmp.add(i*2)
            if int(str(i)+'1') <= B:
                num_tmp.add(int(str(i)+'1'))
        num=num_tmp
        answer+=1

if len(num)==0:
    print(-1)

# B -> A
'''
A,B=map(int,input().split())

answer=0

while B>A:
    if B%2==0:
        B//=2
        answer+=1
    elif B%10==1:
        B//=10
        answer+=1
    else:
        break

if B==A:
    print(answer+1)

else:
    print(-1)   
'''

