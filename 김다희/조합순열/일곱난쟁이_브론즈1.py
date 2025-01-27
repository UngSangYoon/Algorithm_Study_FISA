# 1. 난쟁이 9명의 키를 입력받음.
# 2. com(0,0)을 호출하여 첫 번째 난쟁이부터 탐색 시작.
# 3. 하나의 난쟁이 추가 후 재귀적으로 다음 난쟁이 선택.
# 4. 7명을 선택한 경우 합을 확인.
# 5. 합이 100이면 출력 후 프로그램 종료.
# 6. 합이 100이 아니면 pop()을 사용하여 마지막 선택을 되돌리고 다른 조합 시도.


import sys

N = 9; R = 7 
lst = [int(sys.stdin.readline().strip()) for i in range(N)]
# lst: 난쟁이들 키 리스트 
choose = []

def com(index, level):
    '''
    index: 현재 선택할 난쟁이 위치
    level: 현재 선택된 난쟁이 수
    '''
    if (level == R) and (sum(choose) == 100):
        print(*sorted(choose), sep = "\n")
        sys.exit()
        return
    
    for j in range(index, N): # 현재 위치에서 마지막까지 반복하며, 한 명씩 선택
        choose.append(lst[j]) # 선택한 난쟁이 키 choose 리스트에 추가
        com(j+1, level+1) # 재귀 호출, j+1: 다음 위치로, level+1: 선택한 난쟁이 수 추가
        choose.pop() # 백트래킹

com(0,0)

