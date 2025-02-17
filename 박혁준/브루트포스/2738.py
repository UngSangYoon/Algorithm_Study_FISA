import sys

def main():
    # 행렬 크기 입력
    n, m = map(int, sys.stdin.readline().strip().split())
    
    # 리스트 입력 받기
    list1 = list(map(int, sys.stdin.readline().strip().split()))
    list2 = list(map(int, sys.stdin.readline().strip().split()))
    
    # 입력 데이터 검증
    if len(list1) != n * m or len(list2) != n * m:
        print("Error: Invalid input size")
        return
    
    # 두 리스트의 합 계산
    result = [list1[i] + list2[i] for i in range(n * m)]
    
    # 행렬 형식으로 출력
    for i in range(n):
        print(" ".join(map(str, result[i * m:(i + 1) * m])))

if __name__ == "__main__":
    main()