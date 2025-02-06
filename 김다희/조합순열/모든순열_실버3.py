# N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.
n = int(input())
choose = []
check = [False] * (n+1)

def per(level):
    if level == n:
        print(*choose)
        return
    
    for i in range(1, n+1):
        if check[i] == True:
            continue

        choose.append(i)
        check[i] = True

        per(level+1)

        check[i] = False
        choose.pop()

per(0)