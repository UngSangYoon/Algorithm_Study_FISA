# 메모리 초과로 실행되지 않음
N = int(input())
flag = ['청'] * N

for i in range(1,N +1 ):
    for j in range (1,N+1):
        if i % j == 0:
            if flag[i-1] == '백':
                flag[i-1] = '청'
            else:
                flag[i-1] = '백'
count = flag.count('백')
print(count)

#서칭 후 풀이 1번 깃발 
"""
1번 🔵 → ⚪ (백색)
2번 깃발 🔵 → ⚪ (백색)
3번 깃발 🔵 → ⚪ (백색)
"""