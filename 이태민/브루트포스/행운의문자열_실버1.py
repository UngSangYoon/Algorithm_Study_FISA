'''
문제
민식이와 준영이는 자기 방에서 문자열을 공부하고 있다. 
민식이가 말하길 인접해 있는 모든 문자가 같지 않은 문자열을 행운의 문자열이라고 한다고 한다. 
준영이는 문자열 S를 분석하기 시작했다. 
준영이는 문자열 S에 나오는 문자를 재배치하면 서로 다른 행운의 문자열이 몇 개 나오는지 궁금해졌다. 
만약 원래 문자열 S도 행운의 문자열이라면 그것도 개수에 포함한다.

입력
첫째 줄에 문자열 S가 주어진다. S의 길이는 최대 10이고, 알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 위치를 재배치해서 얻은 서로 다른 행운의 문자열의 개수를 출력한다.

예제 입력 1 
aabbbaa
예제 출력 1 
1
예제 입력 2 
ab
예제 출력 2 
2
예제 입력 3 
aaab
예제 출력 3 
0
예제 입력 4 
abcdefghij
예제 출력 4 
3628800
'''

# 1번 풀이 ->과 메모리 초
# from itertools import permutations  # 순열을 구하기 위한 라이브러리

# s = input()  # 문자열 입력

# # 입력받은 문자열로 만들 수 있는 모든 순열을 구함 (중복 제거)
# s_permutation = set(permutations(s, len(s)))

# lucky_count = 0

# for sub_permutation in s_permutation:
#     # 순열을 문자열로 변환
#     sub_string = ''.join(sub_permutation)
    
#     # 연속된 문자가 있는지 확인
#     has_consecutive = False
    
#     # 순회하면서 연속된 문자가 있는지 확인
#     for j in range(len(sub_string) - 1):
#         if sub_string[j] == sub_string[j + 1]:
#             has_consecutive = True
#             break
    
#     # 연속된 문자가 없다면 lucky_count 증가
#     if not has_consecutive:
#         lucky_count += 1

# print(lucky_count)

# 2번 풀이 -> 백 트래킹을 이용한 풀이
def is_lucky(s):
    # 연속된 문자가 있는지 확인
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True

def backtrack(current, used):
    global lucky_count
    if len(current) == len(s):
        # 완성된 순열이 "럭키"한지 확인
        if is_lucky(current):
            lucky_count += 1
        return
    
    for i in range(len(s)):
        if not used[i]:
            # 같은 문자가 연속으로 선택되지 않도록 방지
            if i > 0 and s[i] == s[i - 1] and not used[i - 1]:
                continue
            
            used[i] = True
            backtrack(current + s[i], used)
            used[i] = False

s = input().strip()
s = ''.join(sorted(s))  # 중복 처리를 위해 정렬
lucky_count = 0
used = [False] * len(s)

backtrack("", used)
print(lucky_count)
