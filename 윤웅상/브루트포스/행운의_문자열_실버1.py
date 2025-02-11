from math import factorial

S = input()
dup = 1
for i in set(S):
    dup *= factorial(S.count(i))

def is_lucky_string(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return 0
    return 1

ans = 0

check = [False] * len(S)
choose = []

def permutation(level):
    global ans

    if not is_lucky_string(choose):
        return

    if level == len(S):
        ans += 1
        return

	# for문
    for i in range(0, len(S)):
        if check[i] == True: # 인덱스가 i인 원소가 이미 사용중이라면 continue
            continue

        choose.append(S[i]) # 인덱스가 i인 원소를 선택(추가) 
        check[i] = True # 인덱스가 i인 원소를 사용하고 있으므로 true로 초기화
        
        permutation(level+1) # 다음 for 문으로 들어가는 역할
        
        check[i] = False # 인덱스가 i인 원소의 사용이 끝났으므로 false로 초기화
        choose.pop() # (넣었던) 인덱스가 i인 원소를 제거

permutation(0)
print(ans//dup)

# 메모리 초과
'''
answer_set = set()

for i in permutations(S):
    answer_set.add(i)

for i in answer_set:
    ans += is_lucky_string(i)

print(ans)
'''