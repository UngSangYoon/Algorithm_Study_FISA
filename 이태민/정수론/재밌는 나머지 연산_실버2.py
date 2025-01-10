# 28138 번
# 첫 번째 시도 -> 메모리 및 시간초과
# N, R = map(int, input().split())

# m_set = set()
# for m in range(1, N + 1):
#     if N % m == R:
#         m_set.add(m)
# print(sum(m_set))

# 두 번째 시도
import math
N, R = map(int, input().split())

def get_primes(N, R):
    m_set = set()
    for m in range(1, int(math.sqrt(N - R)) + 1):
        if (N - R) % m == 0:
            m_set.add(m)
            m_set.add((N - R) // m)
    return sum(set(filter(lambda x:x>R, m_set)))

print(get_primes(N, R))