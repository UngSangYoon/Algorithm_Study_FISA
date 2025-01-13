# 소인수분해
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

# if n == 1: pass 가 없어도 정답
n = int(input())
m = n
list_ = [] # 약수 저장할 리스트
if n == 1:
    pass
else:
    # 약수 리스트 생성 과정
    for i in range(2, n+1):
        if n%i == 0:
            list_.append(i) # 약수 i 리스트 추가
            n = n/i
    # 출력 과정
    for j in range(len(list_)):
        while m%list_[j] == 0:
            print(list_[j])
            m = m/list_[j]
