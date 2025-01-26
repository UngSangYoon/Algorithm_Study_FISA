N = int(input())
R = N
lst = [i for i in range(1,N+1)]
check = [False] * N

choose = []
def permutation(level):
    if level == R:
        for num in choose:
            print(num, end=" ")
        print()
        return

    for i in range(N):
        if check[i]:
            continue

        choose.append(lst[i]) 
        check[i] = True 

        permutation(level + 1)  

        check[i] = False 
        choose.pop() 

permutation(0)
