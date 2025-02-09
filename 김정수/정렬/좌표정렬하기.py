'''
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
'''


n = int(input())

li=[]

for _ in range(n):
    a = list(map(int, input().split()))
    li.append(a)

li.sort()

for i in range(n):
    print(li[i][0], end=" ")
    print(li[i][1])


'''
어차피 좌표는 x,y 두개니까 그냥 for문에서 [i][0], [i][1]으로 출력했습니다.
'''