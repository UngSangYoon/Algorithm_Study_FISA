import sys

# 재귀 함수 정의
def recursion(s, l, r, count):
    count[0] += 1  # 호출 횟수 증가
    if l >= r:
        return 1  # 팰린드롬이면 1 반환
    elif s[l] != s[r]:
        return 0  # 팰린드롬 아니면 0 반환
    else:
        return recursion(s, l + 1, r - 1, count)  # 재귀 호출

# 팰린드롬 여부 판별 함수
def isPalindrome(s):
    count = [0]  # 호출 횟수 추적용 리스트
    result = recursion(s, 0, len(s) - 1, count)  # 재귀 호출 시작
    return result, count[0]  # 결과와 호출 횟수 반환

# 입력 받기 (한 번에 모든 입력을 받음)
input_data = sys.stdin.read().splitlines()  # CTRL+Z로 입력 끝내기

T = int(input_data[0])  # 첫 번째 줄에 테스트 케이스 수 입력

# 각 테스트 케이스 처리
for i in range(1, T + 1):
    s = input_data[i]  # 각 문자열을 입력받음
    result, calls = isPalindrome(s)
    print(result, calls)  # 팰린드롬 여부와 호출 횟수 출력
