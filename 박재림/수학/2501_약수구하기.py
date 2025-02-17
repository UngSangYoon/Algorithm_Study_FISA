p, q = map(int, input().split())  # N, K 입력 받기
yak = []  # 약수를 저장할 리스트

for i in range(1, p + 1):  # 1부터 p까지 반복
    if p % i == 0:  # i가 p의 약수인지 확인
        yak.append(i)  # 약수 리스트에 추가

# K번째 약수가 존재하면 출력, 아니면 0 출력
if len(yak) >= q:
    print(yak[q - 1])  # K번째(인덱스는 q-1) 약수 출력
else:
    print(0)  # 약수가 부족하면 0 출력


