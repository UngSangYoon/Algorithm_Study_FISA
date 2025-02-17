n, k = map(int, input().split())

def kth_get_divider(n, k):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            if count == k:
                return i
    return 0
print(kth_get_divider(n, k))