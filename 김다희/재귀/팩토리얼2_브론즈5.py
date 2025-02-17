# 팩토리얼 2

n = int(input()) 
li = [-1]*(n+3) # 팩토리얼을 담을 리스트
li[0] = 1; li[1] = 1 # 0! = 1, 1! = 1

def fac(x): # 팩토리얼 함수
    if li[x] != -1: # 만약 이미 계산한거면
        return li[x] # 그대로 냅두기
    li[x] = x * fac(x-1) # x자리에 x와 그 전 함수값 곱해서 넣기
    return li[x]

print(fac(n))