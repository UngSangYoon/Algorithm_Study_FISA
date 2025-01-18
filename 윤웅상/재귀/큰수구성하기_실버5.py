'''
문제 18511
N보다 작거나 같은 자연수 중에서, 집합 K의 원소로만 구성된 가장 큰 수를 출력하는 프로그램을 작성하시오. K의 모든 원소는 1부터 9까지의 자연수로만 구성된다.

예를 들어 N=657이고, K={1, 5, 7}일 때 답은 577이다.

입력
첫째 줄에 N, K의 원소의 개수가 공백을 기준으로 구분되어 자연수로 주어진다. (10 ≤ N ≤ 100,000,000, 1 ≤ K의 원소의 개수 ≤ 3)
둘째 줄에 K의 원소들이 공백을 기준으로 구분되어 주어진다. 각 원소는 1부터 9까지의 자연수다.

단, 항상 K의 원소로만 구성된 N보다 작거나 같은 자연수를 만들 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 N보다 작거나 같은 자연수 중에서, K의 원소로만 구성된 가장 큰 수를 출력한다.

예제 입력 1
657 3
1 6 7
예제 출력 1
617
'''
'''
n, k_n = map(int, input().split())
n = str(n)
n = list(map(int, n))
k = list(map(int, input().split()))
k.sort(reverse = True)

if k[0] >= max(n):
    ans = k[0] * len(n-1)
# 경우의 수
# 1. 이전 자리수가 n보다 작음 -> 무조건 큰 수
# 2. 이전 자리수가 n과 같음 -> 현재 자리수가 n과 같거나 작아야함
# 3. 이전 자리수가 n보다 큼 -> 불가능
else:
    flag = False 
    ans = [0] * len(n)
    for digit in range(len(n)): # 각 자리수 탐색
        current = int(n[digit])
        if flag:
            break

        for i in k:
            if current == i:
                ans[digit] = i
                break

            elif current > i:
                ans[digit] = i
                ans[digit+1:] = [k[0]] * (len(ans) - (digit+1))
                flag = True
                break
    
print(''.join(map(str, ans)))

# 위 풀이가 틀릴 수 있는 반례
# 1300 2  
# 3 4
# ans : 444
# 자리수를 줄이는 경우가 불가능함 
# 에외 처리 추가
# 틀렸다느데 왜 틀린지 모르겠음
'''
n, k = map(int, input().split())
arr = sorted(list(map(str, input().split())), reverse=True)  # 큰 수부터 탐색
n_len = len(str(n))  # N의 자릿수

max_result = 0  # 조건을 만족하는 최대값

# 완전탐색: 모든 가능한 조합을 생성
def generate_numbers(current, depth, target_length):
    global max_result

    # target_length에 도달했을 때 검사
    if depth == target_length:
        num = int(current)
        if num <= n:
            max_result = max(max_result, num)
        return

    for digit in arr:
        generate_numbers(current + digit, depth + 1, target_length)

# N과 같은 자릿수부터 탐색
for length in range(n_len, 0, -1):
    generate_numbers("", 0, length)
    if max_result != 0:
        break  # 최대값을 찾으면 바로 종료

print(max_result)
