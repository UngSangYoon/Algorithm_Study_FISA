# combinations 이용 - N이 커지면 느려짐
import sys
import itertools
# 5 0
# -7 -3 -2 5 8
n, s = map(int, sys.stdin.readline().split())  # 정수 개수, 정수
seq = list(map(int, sys.stdin.readline().split()))  # n개의 정수

count = 0
for length in range(1, n+1):  # 부분수열 길이 1부터 n까지 설정해서 탐색
    for sub in itertools.combinations(seq, length):  # n개 원소 중 가능한 모든 조합 생성
        if sum(sub) == s:  
            count += 1 

print(count)