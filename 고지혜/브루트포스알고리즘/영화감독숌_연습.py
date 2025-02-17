# while문으로 풀기
n = int(input())

count = 0  # 찾은 종말의 개수
number = 666 # 제일 작은 종말의 수

while True:
    if "666" in str(number):
        count += 1  
        if count == n:  # n번째 종말의 수를 찾으면
            print(number)  
            break
    
    number += 1  # 다음 숫자로 이동, 모든 숫자 하나씩 검사