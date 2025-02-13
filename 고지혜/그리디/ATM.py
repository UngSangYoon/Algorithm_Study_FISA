n = int(input())  # 사람 수
hap = list(map(int, input().split()))  # 각 사람이 인출하는데 걸리는 시간

# 앞 사람이 오래 걸릴수록 뒤에 있는 사람 대기 시간도 커짐
# => 기다리는 사람 짧은 사람부터 먼저 처리
hap.sort()  # 오름차순

total_sum = 0  # 총 대기 시간 합
wating_sum = 0  # 누적 대기 시간

for time in hap:
    wating_sum += time
    total_sum += wating_sum

print(total_sum)

# n = 5일 때, 입력: 3 1 4 3 2
# 정렬 후 1 2 3 3 4
#   time wainting total
#   1    1        1
#   2    1+2=3    1+3=4  
#   3    3+3=6    4+6=10 
#   3    6+3=9    10+9=19
#   4    9+4=13   19+13=32           