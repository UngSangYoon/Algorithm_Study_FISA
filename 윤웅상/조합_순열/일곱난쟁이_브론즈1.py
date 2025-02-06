'''
lst = []
for _ in range(9):
    t = int(input())
    lst.append(t)
lst.sort()
ans_lst =[]
ans = []
def find_combination(index, level):
    global ans_lst
    if ans_lst:
        return
    
    if level == 7:
        if sum(ans) == 100:
            ans_lst.append(ans)
    
    for i in range(index, 9):
        ans.append(lst[i])
        find_combination(i + 1, level + 1)
        ans.pop()

find_combination(0, 0)
for i in ans_lst[0]:
    print(i)

'''
lst = []
for _ in range(9):
    t = int(input())
    lst.append(t)
lst.sort()
ans = []
def find_combination(index, level):
    if level == 7:
        if sum(ans) == 100:
            for i in ans:
                print(i)
            return True
        return False
    
    for i in range(index, 9):
        ans.append(lst[i])
        if find_combination(i + 1, level + 1):
            return True
        ans.pop()

    return False

find_combination(0, 0)
