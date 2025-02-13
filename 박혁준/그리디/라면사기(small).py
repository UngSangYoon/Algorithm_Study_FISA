# 3
# 1 0 1
def solution(li_, n):
    ans = 0

    for i in range(n):
        if i <= n - 3 and li_[i+1] > li_[i+2]:  
            count = min(li_[i], li_[i+1] - li_[i+2])
            ans += count * 5
            li_[i] -= count
            li_[i+1] -= count

        if i <= n - 3:
            count = min(li_[i], li_[i+1], li_[i+2])
            ans += count * 7
            li_[i] -= count
            li_[i+1] -= count
            li_[i+2] -= count

        if i <= n - 2:
            count = min(li_[i], li_[i+1])
            ans += count * 5
            li_[i] -= count
            li_[i+1] -= count

        # 남은 개수만큼 개별 구매 (3원)
        ans += li_[i] * 3
        li_[i] = 0  # 구매 완료

    return ans








n = int(input())
li_ = list(map(int, input().split()))

print(solution(li_, n))

