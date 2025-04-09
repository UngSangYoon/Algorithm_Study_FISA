n = int(input())
arr = list(map(int, input().split()))

# 누적합 배열 만들기
for i in range(1, n):
    if arr[i] > arr[i] + arr[i-1]:
        arr[i] = arr[i]
    else:
        arr[i] = arr[i] + arr[i-1]
print(max(arr))