num = list(map(int, input().split()))

# print(num)
# for i in range(3):
print((num[0] + num[1]) % num[2])
print((num[0] % num[2]) + (num[1] % num[2]) % num[2])
print((num[0] * num[1]) % num[2])
print((num[0] % num[2]) * (num[1] % num[2]) % num[2])