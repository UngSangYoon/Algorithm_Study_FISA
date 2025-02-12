def backtrack(path, used):
    global ans
    if len(path) == len(S):  # 모든 문자를 사용했을 때
        ans += 1
        return

    prev_char = None  # 중복 방지
    for i in range(len(S)):
        if used[i] or S[i] == prev_char:  # 이미 사용했거나, 중복이면 패스
            continue
        if path and path[-1] == S[i]:  # 인접 중복 체크
            continue

        used[i] = True
        backtrack(path + S[i], used)  # 재귀 호출
        used[i] = False
        prev_char = S[i]  # 중복 체크용

S = sorted(input())  # 정렬된 입력으로 중복 방지
ans = 0
backtrack("", [False] * len(S))
print(ans)