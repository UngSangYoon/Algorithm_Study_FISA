def solution(list1, list2):
    sorted_list1 = sorted(list1)
    sorted_tmp = sorted(range(len(list2)), key=lambda x: list2[x], reverse=True)

    new_list1 = [0] * len(list1)
    for i, idx in enumerate(sorted_tmp):
        new_list1[idx] = sorted_list1[i]

    result = sum(new_list1[i] * list2[i] for i in range(len(list1)))

    
    return result

n = input()
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
print(solution(list1, list2)) 

#####
