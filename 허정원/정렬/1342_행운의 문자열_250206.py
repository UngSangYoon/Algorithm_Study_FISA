'''
문제
민식이와 준영이는 자기 방에서 문자열을 공부하고 있다. 민식이가 말하길 인접해 있는 모든 문자가 같지 않은 문자열을 행운의 문자열이라고 한다고 한다. 준영이는 문자열 S를 분석하기 시작했다. 준영이는 문자열 S에 나오는 문자를 재배치하면 서로 다른 행운의 문자열이 몇 개 나오는지 궁금해졌다. 만약 원래 문자열 S도 행운의 문자열이라면 그것도 개수에 포함한다.

입력
첫째 줄에 문자열 S가 주어진다. S의 길이는 최대 10이고, 알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 위치를 재배치해서 얻은 서로 다른 행운의 문자열의 개수를 출력한다.
'''
# 1 메모리 초과
import itertools
s = input()
# permutations = set(itertools.permutations(s))
done = set()
total_cnt = 0
for perm in itertools.permutations(sorted(s)):
    # if perm in done:
    #     continue

    cnt = 0
    # 하나씩 비교해보기
    for i in range(len(s)-1):
        if perm[i] == perm[i+1]:
            break
        cnt += 1

    if cnt == (len(s)-1):
        total_cnt += 1
        done.add(perm)

print(total_cnt)

# 2 강의코드
from itertools import permutations

def fact(x):
	if x == 0:
		return 1
	return fact(x - 1) * x

S = input()
ans = 0

for perm in permutations(S):
	ok = True
	for i in range(0, len(S) - 1):
		if perm[i] == perm[i + 1]:
			ok = False
			break
	ans += ok

for i in range(ord('a'), ord('z') + 1):
	ans //= fact(S.count(chr(i)))

print(ans)
