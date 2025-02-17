# 거의 소수
# 어떤 수가 소수의 N제곱(N ≥ 2) 꼴일 때, 그 수를 거의 소수라고 한다.
# 두 정수 A와 B가 주어지면, A보다 크거나 같고, B보다 작거나 같은 거의 소수가 몇 개인지 출력한다.
# idea1: 에라토스테네스 체로 소수 찾기 
# idea2: 찾은 소수로 거의 소수 set 만들어서 길이 구하기
# 에라토스테네스 체가 메모리 많이 사용돼서, 다른 부분의 메모리를 최대한 줄여야함
a, b = map(int, input().split())

sosu = [True] * (int(b**(0.5))+1) # 소수 여부
sosu[0], sosu[1] = False, False # 0, 1 제외
almost = set() # 거의 소수

# 에라토스테네스의 체로 소수 리스트 생성
for i in range(2, int(b**(0.5))+1):
    if sosu[i]:
        for j in range(i*i, int(b**(0.5))+1, i):
            sosu[j] = False

prime_list = [p for p in range(2, int(b**(0.5))+1) if sosu[p]]

# 소수 리스트로 거의 소수 set 생성
for p in prime_list:
    if p*p > b: 
        break
    q = p*p
    while q <= b: # 범위 내에서 거의 소수 찾기
        if q >= a:
            almost.add(q)
        q = q*p

print(len(almost))




'''
아래는 메모리 초과 코드
수정1. almost를 리스트가 아니라 set으로 변경
수정2. sosu 리스트 길이 단축

idea: 
1. 에라토스테네스의 체로 소수 찾고,
2. 소수 리스트 저장
3. 소수 리스트 이용해서 거의 소수 세기

a, b = map(int, input().split())

sosu = [True] * (b+1)
sosu[0], sosu[1] = False, False
almost = [False] * (b+1)

for i in range(2, int(b**(0.5))+1):
    if sosu[i]:
        for j in range(i*i, b+1, i):
            sosu[j] = False

prime_list = [p for p in range(2, b+1) if sosu[p]]

for p in prime_list:
    if p*p > b:
        break
    q = p*p
    while q <= b:
        if q >= a:
            almost[q] = True
        q = q*p
        
print(almost[a:b+1].count(True))
'''