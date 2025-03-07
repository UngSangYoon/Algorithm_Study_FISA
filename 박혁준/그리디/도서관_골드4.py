def solution(list_, k):
    list_sorted = sorted(list_, key=abs)

    negative = [x for x in list_sorted if x < 0]
    positive = [x for x in list_sorted if x >= 0]
    
    max_num = max(list_sorted, key=abs)
    
    def foot_sum(li_):
        li_abs = [abs(x) for x in li_]
        li_abs.sort()
        li_len = len(li_abs)

        if li_len % 2 == 1:
            return sum(li_abs[i] for i in range(len(li_abs) - 1, -1, -k))
        else:
            return sum(li_abs[i] for i in range(len(li_abs) - 1, -1, -k))

    result = foot_sum(negative) * 2 + foot_sum(positive) * 2 - abs(max_num)
    return result

n, k = map(int, input().split())
list_ = list(map(int, input().split()))

print(solution(list_, k))

#####