def solution(n):
    len = 1+(n-1)*4
    array[0] = [1] * len(array[0])
    for i in range(1,len-1):
        array[i][0] = 1
        array[i][-1] = 1
    array[-1] = [1] * len(array[-1])
    return (n-1)



# 1+(n-1)*4

n = int(input())
array = [[0]* (1+(n-1)*4)for i in range(1+(n-1)*4)]
for i in array :
    for j in i:
        print(j,end="")
    print()