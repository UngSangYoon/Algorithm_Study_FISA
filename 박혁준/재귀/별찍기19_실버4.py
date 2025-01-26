def solution(n,array,tmp):
    tmp += 1
    if tmp==n :
        array[(len(array[(len(array)//2)])//2)] = "*"
        return array
    else :
        array[0][(len(array)//2)-2*tmp :(len(array)//2)+1+2*tmp]
        return solution(n-1,array,tmp)



# 1+(n-1)*4

n = int(input())
array = [["a"] * (1+(n-1)*4)for i in range(1+(n-1)*4)]

# array = solution(n,array,0)

for i in array :
    for j in i:
        print(f"{j}",end="")
    print()