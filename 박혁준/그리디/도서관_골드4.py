def solution(list_):
    list_sorted = sorted(list_) 
    
    negative = [x for x in list_sorted if x < 0]
    positive = [x for x in list_sorted if x >= 0]

    def foot_sum(li_):
        li_abs = [abs(x) for x in li_]
        li_len = len(li_abs)

        if li_len % 2 == 1:  
            return sum(li_abs[i] for i in range(0, li_len, 2))
        else: 
            return sum(li_abs[i] for i in range(1, li_len, 2))

    return foot_sum(negative) + foot_sum(positive)

n, k = map(int, input().split())
list_ = list(map(int, input().split()


print(solution(list_))
