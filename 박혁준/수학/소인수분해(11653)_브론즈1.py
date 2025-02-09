# n = int(input())
# a = [False, False] + [True] * (n - 1)
# primes = []
# for i in range(2, n + 1):
#     if a[i]:
#         primes.append(i)
#         for j in range(2 * i, n + 1, i):
#             a[j] = False

# def div(k, l):
#     if (k%l)==0:
#         print(l)
#         return div(k//l,l)
#     else :
#         return k

# for i in primes:
#         div(n,i)

n = int(input())
i = 2
while n > 1:
    if (n % i) == 0:
        print(i)
        n = n // i
    else:
        i += 1
        if i*i > n:
            print(n)
            break