def func(s, e, arr):
    tmp = (e - s + 1) // 3  # 구간을 3등분
    if tmp == 0:  # 더 이상 나눌 수 없으면 종료
        return
    for i in range(s + tmp, e - tmp + 1):  # 중간 구간을 공백으로 채움
        arr[i] = ' '
    func(s, s + tmp - 1, arr)  # 왼쪽 구간 재귀 호출
    func(e - tmp + 1, e, arr)  # 오른쪽 구간 재귀 호출

while True:
    try:
        N = int(input())  # 입력
        size = 3**N
        arr = ['-' for _ in range(size)]  # 길이가 3^N인 배열 생성
        func(0, size - 1, arr)  # 전체 구간 처리
        print(''.join(arr))  # 결과 출력
    except EOFError:  # 입력이 없으면 종료
        break

'''EOF 에러를 처리하는것 까먹고 못했었음'''