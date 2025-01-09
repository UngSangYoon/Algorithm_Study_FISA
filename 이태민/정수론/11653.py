n = int(input())

def get_primes(n):
    primes = []
    for i in range(2, n + 1):
        while n % i == 0:
            primes.append(i)
            n //= i
    return primes

for j in get_primes(n): print(j)