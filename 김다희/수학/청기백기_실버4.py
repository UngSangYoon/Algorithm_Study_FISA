# 청기 백기
# 규칙 찾아서 해결

n = int(input())

for i in range(1, 45827): # 45827 = sqrt(2,100,000,000)
    if i**2 <= n <= (i+1)**2-1: 
        ans = i
        break

print(ans)



'''
아래는 메모리 에러
0과 1을 왔다갔다하는 코드...

n = int(input())
g = [0]*n 
num = 1

while num <= n:
    for i in range(n): 
        if ((i+1) % (num) == 0) & (g[i] == 0):
            g[i] = 1 # 백기
        elif ((i+1) % (num) == 0) & (g[i] == 1):
            g[i] = 0 # 청기
        else:
            pass
    num = num + 1
        
print(sum(g))
'''


