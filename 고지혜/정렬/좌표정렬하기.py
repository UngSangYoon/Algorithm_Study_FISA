# 1. 단순 input() 사용 
# input_ = int(input())  # 점 개수 입력
# n = [tuple(map(int, input().split())) for _ in range(input_)]

# n = sorted(n, key=lambda x: (x[0], x[1]))

# for x, y in n:
#     print(x, y)
# => 점의 개수가 많아지면 성능 느려짐.

# -------------------------------------------------------------------------

# 2. readline()
import sys

input_ = int(sys.stdin.readline().strip())  # 점 개수
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(input_)]

n = sorted(points, key=lambda x : (x[0], x[1]))

for x, y in n:
    print(x, y)

# -------------------------------------------------------------------------

# 3. readlimes(): 
# 문제에서 입력 제한 없기 때문에 큰 입력에는 비효율적인 readlines는 사용하지 않기
# import sys

# lines = sys.stdin.readlines()  # 모든 줄 리스트로 읽기

# input_ = int(lines[0].strip())  # 첫 번째 줄: 점 개수
# points = [tuple(map(int, line.split())) for line in lines[1:]]

# n = sorted(points, key=lambda x : (x[0], x[1]))

# for x, y in n:
#     print(x, y)