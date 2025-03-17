'''
< 버튼을 K번 눌렀을 때, 화면에 A와 B의 개수는 몇 개일까? >
# 처음은 A로 화면에 표시
# '모든'
    - B는 BA로 바뀜
    - A는 B로 바뀜
=> A와 B의 개수는 공백으로 구분하여 출력하기
'''
# def babba(k):
#     # 편하게 a는 0으로, b는 1로
#     a, b = 0, 1
#     for _ in range(k-1):  # 이미 A로 시작하기 때문에 k=0이 시작점
#         a, b = b, a + b
#     print(a, b)

# k = int(input())
# babba(k)
'''
k  A   B
0  1   0    A
1  0   1    B
2  1   1    BA
3  1   1+1  BA/B
4  1+1 2+1  BA/B/BA
5  2+1 3+2  BA/B/BA/BA/B
'''
def babba(k):
    if k == 0:
        return (1, 0)
    elif k == 1:
        return (0, 1)
    
    # for문을 재귀로
    a, b = babba(k-1)
    return (b, a + b)

k = int(input())
a, b = babba(k)
print(a, b)