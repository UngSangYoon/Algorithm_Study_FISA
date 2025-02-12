n = int(input())

for i in range(n):
    num = n//2 + i
    str_num = list(map(int, str(num)))
    num_sum = num + sum(str_num)
    if num_sum == n:
        print(num)
        break
    if i == n-1:
        print(0)