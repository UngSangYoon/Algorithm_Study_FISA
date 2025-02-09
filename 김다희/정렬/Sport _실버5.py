import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
result = sorted(li, key=lambda x: (x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))
print(" ".join(str(x[0]) for x in result[:3]))

# 강의 풀이 코드 출력 부분이 더 직관적일지도...?
# for b, p, q, r in infos[:3]:
#     print(b, end=' ')
