def func(idx, choose):
    if idx == N:  # 모든 원소를 다 확인한 경우
        if len(choose)>0 and sum(choose)==S:
            return 1
        else:
            return 0


    # 현재 원소를 선택하는 경우
    choose.append(arr[idx])
    cnt1 = func(idx + 1, choose)
    choose.pop()

    # 현재 원소를 선택하지 않는 경우
    cnt2 = func(idx + 1, choose)

    return cnt1 + cnt2  # 선택한 경우와 선택하지 않은 경우의 합을 반환


# 입력 받기
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 결과 출력
print(func(0, []))  # choose 리스트를 매개변수로 전달