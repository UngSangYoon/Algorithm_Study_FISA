'''
< 
- 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있음
    - 한 계단을 밟으면서 이어서 다음 계단 x
    - 다음 다음 계단 o1
    - 연속된 세 개의 계단을 모두 밟기 x  
- 시작점은 계단에 포함 x
- 마지막 도착 계단은 반드시 밟기 o
=> 얻을 수 있는 총 점수의 최댓값 구하기
'''
num = int(input())  # 5
scores = [int(input()) for _ in range(num)]  # 10 20 15 25 10

if num == 1:  # 한 칸이면 바로 출력
    print(scores[0])
elif num == 2:  # 두 칸이면 시작과 마지막밖에 없으니까 더한 거 출력
    print(scores[0] + scores[1])
else:
    total_score = [0] * num
    total_score[0] = scores[0]
    total_score[1] = scores[0] + scores[1]
    # 시작+마지막 or (시작+1)+마지막
    total_score[2] = max(scores[0] + scores[2], scores[1] + scores[2])
    for i in range(3, num):  # num= 3 4
        total_score[i] = max(
            total_score[i-2] + scores[i],
            total_score[i-3] + scores[i-1] + scores[i]
        )
    print(total_score[-1])

'''
0   1   2   3   4   
10  20  15  25  10  

total_score = [0, 0, 0, 0, 0]
total_score[0] = scores[0] -> total_score = [10, 0, 0, 0, 0]
total_score[1] = scores[0] + scores[1] -> total_score = [10, 30, 0, 0, 0]
total_score[2] = max(scores[0] + scores[2], scores[1] + scores[2]) 여기서는 1+2가 크므로 35
                -> total_score = [10, 30, 35, 0, 0]

total_score[3] - 0+1+3, 0+1은 total_score[1]이므로 total_score[1]+scores[3] 
               or 0+2+3, total_scores[i-3] + scores[i-1] + scores[i]     
               두 개의 값 중 큰 것으로 
               -> 여기서는 0+1+3이 크므로 55 -> total_score[10, 30, 35, 55, 0]
total_score[4] - 0+2+4, 0+2는 total_score[2]이므로 total_score[2]+scores[4]=35+10=45
               or 0+1+3+4, total_scores[i-3] + scores[i-1] + scores[i]=30+25+10=65    
               -> 여기서는 0+1+3+4가 크므로 65 -> total_score = [10, 30, 35, 55, 65]  
'''